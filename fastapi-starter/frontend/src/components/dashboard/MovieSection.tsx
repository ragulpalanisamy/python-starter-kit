import { Card, CardBody, CardHeader, Popover, PopoverContent, PopoverTrigger } from "@heroui/react";
import { Clock, Film, Info, Star } from "lucide-react";
import { useState } from "react";

import { useGetMoviesQuery } from "../../store/moviesApi";
import { Chip, LoadingSpinner, Pagination, RefetchButton } from "../shared";

export const MovieSection = () => {
  const [page, setPage] = useState(1);
  const pageSize = 5;
  const { data: movieData, isLoading, isFetching, refetch } = useGetMoviesQuery({ page, pageSize });

  return (
    <Card className="bg-white/5 border-slate-700/20 backdrop-blur-xl h-full shadow-2xl transition-all duration-300 rounded-lg">
      <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
        <div className="flex gap-2.5 items-center min-w-0">
          <div className="bg-white/10 p-1.5 rounded-lg shadow-lg shrink-0 transition-transform duration-200 hover:scale-105">
            <Film className="text-white" size={16} />
          </div>
          <div className="min-w-0">
            <p className="text-sm font-semibold text-white truncate">Cinema Catalog</p>
            <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase truncate">
              MFlix Database
            </p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          {movieData && (
            <Chip size="sm" variant="flat" className="font-semibold text-[8px]">
              {movieData.total}
            </Chip>
          )}
          <RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />
        </div>
      </CardHeader>

      <CardBody className="px-2 pb-2 pt-0 flex flex-col h-full gap-2">
        <div className="flex-1 min-h-[300px] relative">
          {(isFetching || isLoading) && (
            <div>
              <LoadingSpinner size="sm" />
            </div>
          )}
          <div className={isFetching || isLoading ? "opacity-50 pointer-events-none" : ""}>
            <div className="space-y-1">
              {movieData?.items.map((movie, index) => (
                <div
                  key={movie.id}
                  className={`bg-white/5 border border-slate-700/20 p-2 rounded-lg flex justify-between items-center group hover:bg-white/10 hover:border-slate-600/30 transition-all gap-1 ${index > 0 ? "mt-1" : ""}`}
                >
                  <div className="flex items-center gap-2 overflow-hidden min-w-0 flex-1">
                    <div className="bg-white/10 h-8 w-8 rounded-lg flex items-center justify-center border border-slate-600/20 group-hover:bg-white/20 transition-all shrink-0 overflow-hidden">
                      {movie.poster ? (
                        <img
                          src={movie.poster}
                          alt={movie.title}
                          className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                        />
                      ) : (
                        <Film size={12} className="text-white" />
                      )}
                    </div>
                    <div className="overflow-hidden min-w-0 flex-1">
                      <h3 className="font-semibold text-white text-xs truncate">{movie.title}</h3>
                      <div className="flex items-center gap-1 wrap">
                        <Chip size="sm" variant="flat" className="text-[7px] font-semibold">
                          {movie.year}
                        </Chip>
                        <div className="flex items-center gap-0.5 text-[9px] text-amber-400 font-semibold">
                          <Star size={8} fill="currentColor" className="text-amber-400" />
                          {movie.imdb?.rating || "N/A"}
                        </div>
                        {movie.runtime && (
                          <div className="flex items-center gap-0.5 text-[9px] text-slate-400">
                            <Clock size={8} />
                            {movie.runtime}m
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  <Popover placement="left" showArrow offset={10}>
                    <PopoverTrigger>
                      <button className="text-slate-400 hover:text-white transition-colors p-1 shrink-0">
                        <Info size={14} />
                      </button>
                    </PopoverTrigger>
                    <PopoverContent className="bg-slate-950/95 border-slate-700/20 p-2 max-w-[250px] backdrop-blur-xl rounded-lg">
                      <div className="space-y-2">
                        <p className="text-xs font-semibold text-white uppercase tracking-wide">Synopsis</p>
                        <p className="text-[10px] text-slate-300 leading-relaxed italic">
                          {movie.plot || "No description available."}
                        </p>
                        <div className="pt-2 flex wrap gap-1">
                          {movie.genres.map((g, idx) => (
                            <Chip
                              key={g}
                              size="sm"
                              variant="flat"
                              className={`text-[7px] ${idx > 0 ? "ml-1" : ""}`}
                            >
                              {g}
                            </Chip>
                          ))}
                        </div>
                      </div>
                    </PopoverContent>
                  </Popover>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="flex justify-center items-center pt-1">
          <Pagination
            total={movieData?.total_pages || 1}
            page={page}
            onChange={setPage}
            size="sm"
            showControls
          />
        </div>
      </CardBody>
    </Card>
  );
};
