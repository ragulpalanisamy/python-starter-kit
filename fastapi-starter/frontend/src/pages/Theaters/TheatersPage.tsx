import { Card, CardBody } from "@heroui/react";
import { Navigation, MapPin, Hash } from "lucide-react";
import { useState } from "react";
import { useGetTheatersQuery } from "../../store/theatersApi";
import { PageHeader, LoadingSpinner, RefetchButton, Button, Chip, Pagination } from "../../components/shared";
import { PAGE_SIZES } from "../../constants";

export const TheatersPage = () => {
  const [page, setPage] = useState(1);
  const { data, isLoading, isFetching, refetch } = useGetTheatersQuery({
    page,
    pageSize: PAGE_SIZES.THEATERS,
  });

  return (
    <div className="space-y-2">
      <PageHeader
        title="Cinema Network"
        description="Global distribution of MFlix exhibition partner locations"
        action={<RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />}
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
                <LoadingSpinner size="lg" label="Loading theaters..." />
              </div>
            ) : data?.items.length === 0 ? (
              <div className="text-center py-16 opacity-30 flex flex-col items-center gap-2">
                <MapPin size={48} className="text-white" />
                <p className="text-sm font-bold uppercase tracking-wide text-white">No Theaters Found</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
                {(data?.items || []).map((theater, index) => (
                  <div
                    key={theater.id}
                    className={`bg-white/5 border border-slate-700/20 rounded-lg p-2 hover:bg-white/10 hover:border-slate-600/30 transition-all group ${index > 0 ? "mt-1" : ""}`}
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <div className="w-12 h-12 rounded-lg bg-white/10 flex items-center justify-center border border-slate-600/20 shrink-0 group-hover:bg-white/20 transition-all">
                        <Hash size={18} className="text-white font-mono font-bold" />
                      </div>
                      <div className="min-w-0 flex-1">
                        <p className="font-semibold text-white text-sm">Venue #{theater.theaterId}</p>
                        <p className="text-[9px] font-mono text-slate-400">ID: {theater.theaterId}</p>
                      </div>
                    </div>

                    <div className="space-y-1 mb-2">
                      <div className="space-y-1">
                        <p className="text-xs font-semibold text-white truncate">
                          {theater.location.address.street1}
                        </p>
                        <p className="text-[10px] text-slate-400 uppercase tracking-wide font-medium truncate">
                          {theater.location.address.city}, {theater.location.address.state}{" "}
                          {theater.location.address.zipcode}
                        </p>
                      </div>

                      <div className="flex items-center">
                        <Chip size="sm" variant="flat" className="text-[8px] font-mono">
                          {theater.location.geo.coordinates[0].toFixed(4)},{" "}
                          {theater.location.geo.coordinates[1].toFixed(4)}
                        </Chip>
                      </div>
                    </div>

                    <div className="flex items-center">
                      <Button
                        size="sm"
                        variant="flat"
                        className="font-semibold text-[9px] uppercase tracking-wide w-full"
                        startContent={<Navigation size={10} />}
                      >
                        View Map
                      </Button>
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
