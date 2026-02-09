import { useState } from "react";
import { Card, CardBody, CardHeader, Progress } from "@heroui/react";
import { Send, Sparkles } from "lucide-react";
import { usePredictSentimentMutation } from "../../store/mlApi";
import { toast } from "react-hot-toast";
import { FormField, LoadingSpinner, Button, Chip } from "../shared";

export const SentimentSection = () => {
  const [text, setText] = useState("");
  const [predictSentiment, { data: prediction, isLoading: predicting }] = usePredictSentimentMutation();

  const handlePredict = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) return;

    try {
      await predictSentiment({ text }).unwrap();
      toast.success("Analysis complete");
    } catch {
      toast.error("Prediction failed");
    }
  };

  const isPositive = prediction?.sentiment === "POSITIVE";
  const isNegative = prediction?.sentiment === "NEGATIVE";

  return (
    <Card className="bg-linear-to-br from-purple-500/10 via-white/5 to-blue-500/10 border-2 border-purple-500/30 backdrop-blur-xl h-full shadow-2xl transition-all duration-300 hover:border-purple-500/50 hover:shadow-purple-500/20 rounded-lg">
      <CardHeader className="flex gap-2 p-2 border-b border-purple-500/20 bg-linear-to-r from-purple-500/5 to-transparent">
        <div className="bg-linear-to-br from-purple-500/30 to-blue-500/30 p-1 rounded-lg shadow-lg shrink-0 transition-transform duration-200 hover:scale-105 ring-2 ring-purple-500/20">
          <Sparkles className="text-white" size={16} />
        </div>
        <div className="min-w-0">
          <p className="text-sm font-bold truncate bg-linear-to-r from-purple-300 to-blue-300 bg-clip-text text-transparent">
            Intelligence Engine
          </p>
          <p className="text-[9px] text-purple-300/80 font-semibold tracking-wide uppercase truncate">
            Neural Sentiment Analysis
          </p>
        </div>
      </CardHeader>

      <CardBody className="px-2 pb-2 pt-2 min-h-[200px]">
        <form onSubmit={handlePredict} className="space-y-2">
          <div className="relative min-h-[120px]">
            {predicting && (
              <div className="absolute inset-0 flex items-center justify-center bg-slate-950/50 backdrop-blur-sm rounded-lg z-10">
                <LoadingSpinner size="md" label="Analyzing..." />
              </div>
            )}
            <FormField
              type="textarea"
              label="Enter Text"
              value={text}
              onChange={setText}
              placeholder="Enter text to analyze sentiment..."
              minRows={4}
              className={predicting ? "opacity-50 pointer-events-none" : ""}
            />
          </div>
          <div className="flex justify-end items-center gap-1">
            <Button
              type="submit"
              size="md"
              variant="flat"
              isLoading={predicting}
              isDisabled={predicting}
              startContent={!predicting && <Send size={14} />}
              className="min-w-[120px]"
            >
              Analyze Text
            </Button>
          </div>
        </form>

        {prediction && (
          <div className="mt-2 p-2 rounded-lg backdrop-blur-sm border border-slate-700/20 bg-white/5 transition-all duration-300 hover:bg-white/10 hover:border-slate-600/30">
            <div className="flex items-start gap-2">
              <div
                className={`w-1 h-full min-h-[80px] rounded-full shrink-0 ${
                  isPositive ? "bg-green-500/40" : isNegative ? "bg-red-500/40" : "bg-slate-500/40"
                }`}
              />
              <div className="flex-1 min-w-0">
                <div className="flex justify-between items-center mb-2 gap-1">
                  <Chip
                    variant="flat"
                    size="md"
                    className="font-semibold text-[10px] uppercase bg-white/10 text-white border border-slate-600/20"
                  >
                    {prediction.sentiment}
                  </Chip>
                  <span className="text-[9px] font-mono text-slate-400 uppercase tracking-wide whitespace-nowrap">
                    {prediction.processing_time_ms}ms
                  </span>
                </div>

                <p className="italic mb-2 leading-relaxed text-xs line-clamp-3 text-wrap text-slate-200">
                  "{prediction.text}"
                </p>

                <div className="space-y-2">
                  <div className="flex justify-between items-center text-[10px] font-semibold text-slate-400 uppercase tracking-wide">
                    <span>Confidence</span>
                    <span className="font-bold text-white">
                      {(prediction.confidence * 100).toFixed(1)}%
                    </span>
                  </div>
                  <Progress
                    value={prediction.confidence * 100}
                    className="h-2"
                    size="sm"
                    classNames={{
                      indicator: isPositive ? "bg-green-500/60" : isNegative ? "bg-red-500/60" : "bg-white/30",
                      track: "bg-white/10",
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
        )}
      </CardBody>
    </Card>
  );
};
