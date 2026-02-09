import { useState } from "react";
import { Card, CardBody, CardHeader, ScrollShadow } from "@heroui/react";
import { History, Clock, TrendingUp } from "lucide-react";
import { useGetPredictionHistoryQuery } from "../../store/mlApi";
import { LoadingSpinner, RefetchButton, Chip, Pagination } from "../shared";

export const MLHistorySection = () => {
  const [page, setPage] = useState(1);
  const pageSize = 10;
  const {
    data: historyData,
    isLoading,
    isFetching,
    refetch,
  } = useGetPredictionHistoryQuery({
    page,
    pageSize,
  });

  const isPositive = (sentiment: string) => sentiment === "POSITIVE";
  const isNegative = (sentiment: string) => sentiment === "NEGATIVE";

  return (
    <Card className="bg-white/5 border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
      <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
        <div className="flex gap-2 items-center min-w-0">
          <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
            <History className="text-white" size={16} />
          </div>
          <div className="min-w-0">
            <p className="text-sm font-bold text-white truncate">Prediction History</p>
            <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase truncate">
              Sentiment Analysis Log
            </p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          {historyData && (
            <Chip size="sm" variant="flat" className="font-semibold text-[8px]">
              {historyData.predictions.length}
            </Chip>
          )}
          <RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />
        </div>
      </CardHeader>

      <CardBody className="px-2 pb-2 pt-2 flex flex-col h-full gap-2">
        <ScrollShadow className="flex-1 max-h-[400px] min-h-[300px]">
          <div className="relative min-h-[300px]">
            {isFetching && (
              <div className="absolute inset-0 flex items-center justify-center bg-slate-950/30 backdrop-blur-sm rounded-lg z-10">
                <LoadingSpinner size="sm" />
              </div>
            )}
            <div className={`space-y-1 pr-2 ${isFetching ? "opacity-50 pointer-events-none" : ""}`}>
              {isLoading ? (
                <div className="flex items-center justify-center py-10">
                  <LoadingSpinner size="md" label="Loading history..." />
                </div>
              ) : historyData?.predictions.length === 0 ? (
                <div className="text-center py-10 opacity-30 flex flex-col items-center gap-2">
                  <History size={32} className="text-white" />
                  <p className="text-[9px] font-bold uppercase tracking-wide text-white">No History</p>
                </div>
              ) : (
                historyData?.predictions.map((prediction, index) => (
                  <div
                    key={prediction.prediction_id}
                    className={`p-2 rounded-lg border border-slate-700/20 bg-white/5 transition-all duration-200 hover:border-slate-600/30 hover:bg-white/10 ${
                      index > 0 ? "mt-1" : ""
                    }`}
                  >
                    <div className="flex justify-between items-center mb-2 gap-2">
                      <div className="flex items-center gap-2">
                        <div
                          className={`w-1 h-6 rounded-full shrink-0 ${
                            isPositive(prediction.sentiment)
                              ? "bg-green-500/40"
                              : isNegative(prediction.sentiment)
                                ? "bg-red-500/40"
                                : "bg-slate-500/40"
                          }`}
                        />
                        <Chip
                          variant="flat"
                          size="sm"
                          className="font-semibold text-[8px] uppercase bg-white/10 text-white border-slate-600/20"
                        >
                          {prediction.sentiment}
                        </Chip>
                      </div>
                      <div className="flex items-center gap-1 text-[8px] text-slate-400">
                        <Clock size={8} />
                        <span className="font-mono">{prediction.processing_time_ms}ms</span>
                      </div>
                    </div>

                    <p className="text-xs leading-relaxed mb-2 line-clamp-2 text-slate-200">
                      "{prediction.text}"
                    </p>

                    <div className="flex justify-between items-center">
                      <div className="flex items-center gap-1.5">
                        <TrendingUp size={10} className="text-slate-400" />
                        <span className="text-[9px] font-semibold text-white">
                          {(prediction.confidence * 100).toFixed(1)}%
                        </span>
                      </div>
                      <span className="text-[8px] font-mono text-slate-500">
                        {new Date(prediction.created_at).toLocaleDateString()}
                      </span>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </ScrollShadow>

        {historyData && (
          <div className="flex justify-center items-center pt-1">
            <Pagination total={page + 1} page={page} onChange={setPage} size="sm" showControls />
          </div>
        )}
      </CardBody>
    </Card>
  );
};
