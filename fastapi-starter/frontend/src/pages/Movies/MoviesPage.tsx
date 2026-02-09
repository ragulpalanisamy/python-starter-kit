import { Card, CardBody } from "@heroui/react";
import { Film, Star, Clock } from "lucide-react";
import { useState } from "react";
import { useGetMoviesQuery } from "../../store/moviesApi";
import {
  PageHeader,
  SearchInput,
  LoadingSpinner,
  RefetchButton,
  Chip,
  Pagination,
} from "../../components/shared";
import { PAGE_SIZES } from "../../constants";

export const MoviesPage = () => {
  const [page, setPage] = useState(1);
  const [searchQuery, setSearchQuery] = useState("");
  const { data, isLoading, isFetching, refetch } = useGetMoviesQuery({
    page,
    pageSize: PAGE_SIZES.MOVIES,
  });

  return (
    <div className="space-y-2">
      <PageHeader
        title="Movies Repository"
        description="Explore the MFlix global cinema database"
        action={
          <div className="flex items-center gap-2">
            <SearchInput
              placeholder="Search movies..."
              value={searchQuery}
              onChange={setSearchQuery}
              className="w-full sm:w-64"
            />
            <RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />
          </div>
        }
      />

      <Card className="bg-white/5 border-slate-700/20 backdrop-blur-xl shadow-2xl overflow-hidden rounded-lg">
        <CardBody className="p-2 relative min-h-[400px]">
          {isFetching && (
            <div className="absolute inset-0 flex items-center justify-center bg-slate-950/30 backdrop-blur-sm z-10 rounded-lg">
              <LoadingSpinner size="md" />
            </div>
          )}
          <div className={isFetching ? "opacity-50 pointer-events-none" : ""}>
            {isLoading ? (
              <div className="flex items-center justify-center py-16">
                <LoadingSpinner size="lg" label="Loading movies..." />
              </div>
            ) : data?.items.length === 0 ? (
              <div className="text-center py-16 opacity-30 flex flex-col items-center gap-2">
                <Film size={48} className="text-white" />
                <p className="text-sm font-bold uppercase tracking-wide text-white">No Movies Found</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-2">
                {(data?.items || []).map((movie, index) => (
                  <div
                    key={movie.id}
                    className={`bg-white/5 border border-slate-700/20 rounded-lg p-2 hover:bg-white/10 hover:border-slate-600/30 transition-all group cursor-pointer ${index > 0 ? "mt-1" : ""}`}
                  >
                    <div className="flex gap-2 mb-2">
                      <div className="w-16 h-24 bg-white/10 rounded-lg overflow-hidden shrink-0 group-hover:scale-105 transition-transform duration-300 border border-slate-700/20">
                        {movie.poster ? (
                          <img src={movie.poster} alt={movie.title} className="w-full h-full object-cover" />
                        ) : (
                          <div className="w-full h-full flex items-center justify-center">
                            <Film size={20} className="text-white" />
                          </div>
                        )}
                      </div>
                      <div className="min-w-0 flex-1">
                        <h3 className="font-semibold text-white group-hover:text-white transition-colors text-sm truncate mb-1">
                          {movie.title}
                        </h3>
                        <p className="text-[10px] font-mono text-slate-400 mb-2">{movie.year}</p>
                        <div className="flex items-center gap-1.5">
                          <Star size={12} className="text-amber-400 fill-amber-400" />
                          <span className="font-semibold text-xs text-white">
                            {movie.imdb?.rating || "N/A"}
                          </span>
                        </div>
                      </div>
                    </div>

                    <div className="space-y-2">
                      <div className="flex items-center wrap gap-1">
                        {movie.genres.slice(0, 3).map((genre, idx) => (
                          <Chip
                            key={genre}
                            variant="flat"
                            size="sm"
                            className={`text-[9px] font-semibold uppercase ${idx > 0 ? "ml-1" : ""}`}
                          >
                            {genre}
                          </Chip>
                        ))}
                      </div>
                      {movie.directors.length > 0 && (
                        <p className="text-xs text-slate-300 truncate">
                          <span className="text-slate-500">Dir: </span>
                          {movie.directors.join(", ")}
                        </p>
                      )}
                      {movie.runtime && (
                        <div className="flex items-center gap-1 text-[10px] text-slate-400">
                          <Clock size={10} />
                          {movie.runtime}m
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {data && data.total_pages > 1 && (
            <div className="flex w-full justify-center items-center pt-2 mt-2 border-t border-slate-700/20">
              <Pagination
                isCompact
                showControls
                page={page}
                total={data.total_pages}
                onChange={setPage}
                size="sm"
              />
            </div>
          )}
        </CardBody>
      </Card>
    </div>
  );
};
