import { Card, CardBody, CardHeader, Divider, Progress, Spinner } from "@heroui/react";
import { motion } from "framer-motion";
import { Activity, BrainCircuit, Clock, Cpu, Send } from "lucide-react";
import { useState } from "react";
import { toast } from "react-hot-toast";
import { MLHistorySection } from "../../components/dashboard/MLHistorySection";
import { MLStatsDashboard } from "../../components/dashboard/MLStatsDashboard";
import { Button, Chip, FormField, PageHeader } from "../../components/shared";
import { useGetMLStatsQuery, useGetModelInfoQuery, usePredictSentimentMutation } from "../../store/mlApi";

export const MLPage = () => {
  const [text, setText] = useState("");
  const { data: modelInfo } = useGetModelInfoQuery();
  const [predictSentiment, { data: prediction, isLoading: predicting }] = usePredictSentimentMutation();

  const { data: stats, isLoading: statsLoading, isFetching: statsFetching, refetch: refetchStats, error: statsError } = useGetMLStatsQuery(undefined, {
    refetchOnMountOrArgChange: true,
  });


  const handlePredict = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) return;

    try {
      await predictSentiment({ text }).unwrap();
      toast.success("Intelligence analysis complete");
    } catch {
      toast.error("Prediction sequence failed");
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-2">
      <PageHeader
        title="Neural Interface"
        description="Advanced NLP Sentiment Classification Engine"
        icon={
          <div className="p-1 bg-white/10 rounded-lg shrink-0 border border-slate-700/20">
            <BrainCircuit className="text-white" size={20} />
          </div>
        }
        action={
          modelInfo && (
            <div className="text-right">
              <p className="text-[9px] font-semibold text-slate-400 uppercase tracking-wide">Device</p>
              <div className="flex items-center gap-1 justify-end">
                <span className="w-1 h-1 rounded-full bg-white" />
                <p className="text-xs font-semibold text-white uppercase">{modelInfo.device}</p>
              </div>
            </div>
          )
        }
      />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-2">
        <Card className="lg:col-span-2 bg-white/5 border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex gap-2 p-2">
            <Cpu className="text-white" size={18} />
            <h3 className="text-base font-semibold text-white">Input Sequence</h3>
          </CardHeader>
          <Divider className="bg-white/10" />
          <CardBody className="p-2 space-y-2">
            <form onSubmit={handlePredict} className="space-y-2">
              <div className="w-full">
                <FormField
                  type="textarea"
                  label="Analyze Commentary"
                  value={text}
                  onChange={setText}
                  placeholder="Paste text here to evaluate sentiment polarity..."
                  minRows={5}
                />
              </div>
              <div className="w-full flex justify-end items-center">
                <Button
                  type="submit"
                  size="md"
                  variant="flat"
                  isLoading={predicting}
                  startContent={!predicting && <Send size={14} />}
                  className="min-w-[160px]"
                >
                  Execute Inference
                </Button>
              </div>
            </form>
          </CardBody>
        </Card>

        <div className="space-y-2">
          <Card className="bg-white/5 border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
            <CardHeader className="flex gap-2 p-2">
              <Activity className="text-white" size={16} />
              <h3 className="text-xs font-semibold uppercase tracking-wide text-slate-400">Model Meta</h3>
            </CardHeader>
            <CardBody className="px-2 pb-2 pt-0 space-y-2">
              {modelInfo ? (
                <>
                  <div className="p-2 bg-white/5 rounded-lg border border-slate-700/20 backdrop-blur-sm">
                    <p className="text-[8px] font-semibold text-slate-400 uppercase mb-1">Architecture</p>
                    <p className="text-xs font-semibold text-white truncate">{modelInfo.model_name}</p>
                  </div>
                  <div className="p-2 bg-white/5 rounded-lg border border-slate-700/20 backdrop-blur-sm">
                    <p className="text-[8px] font-semibold text-slate-400 uppercase mb-1">Framework</p>
                    <p className="text-xs font-semibold text-white">{modelInfo.framework} v2.0</p>
                  </div>
                </>
              ) : (
                <Spinner size="sm" />
              )}
            </CardBody>
          </Card>

          {prediction && (
            <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }}>
              <Card className="border border-slate-700/20 bg-white/5 backdrop-blur-xl shadow-2xl transition-all duration-300 hover:bg-white/10 hover:border-slate-600/30 rounded-lg">
                <CardBody className="p-2">
                  <div className="flex items-start gap-2">
                    <div
                      className={`w-1 h-full min-h-[80px] rounded-full shrink-0 ${
                        prediction.sentiment === "POSITIVE"
                          ? "bg-green-500/40"
                          : prediction.sentiment === "NEGATIVE"
                            ? "bg-red-500/40"
                            : "bg-slate-500/40"
                      }`}
                    />
                    <div className="flex-1 min-w-0">
                      <div className="flex justify-between items-center mb-2 gap-2">
                        <Chip
                          variant="flat"
                          size="md"
                          className="font-semibold text-[10px] uppercase bg-white/10 text-white border border-slate-600/20"
                        >
                          {prediction.sentiment}
                        </Chip>
                        <div className="flex items-center gap-1 text-[9px] font-semibold text-slate-400 uppercase tracking-wide whitespace-nowrap">
                          <Clock size={10} />
                          {prediction.processing_time_ms}ms
                        </div>
                      </div>

                      <div className="space-y-2">
                        <div className="flex justify-between text-[10px] font-semibold text-slate-400 uppercase tracking-wide">
                          <span>Confidence</span>
                          <span className="font-bold text-white">
                            {(prediction.confidence * 100).toFixed(2)}%
                          </span>
                        </div>
                        <Progress
                          value={prediction.confidence * 100}
                          className="h-1.5"
                          size="sm"
                          classNames={{
                            indicator:
                              prediction.sentiment === "POSITIVE"
                                ? "bg-green-500/60"
                                : prediction.sentiment === "NEGATIVE"
                                  ? "bg-red-500/60"
                                  : "bg-white/30",
                            track: "bg-white/10",
                          }}
                        />
                      </div>
                    </div>
                  </div>
                </CardBody>
              </Card>
            </motion.div>
          )}
        </div>
      </div>

      <motion.section
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.3 }}
        className="mt-2"
      >
        <MLStatsDashboard stats={stats} isLoading={statsLoading} isFetching={statsFetching} error={statsError} onRefetch={refetchStats} />
      </motion.section>

      <motion.section
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.4 }}
        className="mt-2"
      >
        <MLHistorySection />
      </motion.section>
    </div>
  );
};
