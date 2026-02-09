import { api } from "./api";
import type { PredictionResult, ModelInfo } from "../types";

export interface PredictionHistoryResponse {
  predictions: PredictionResult[];
  skip: number;
  limit: number;
}

export interface MLStatsResponse {
  total: number;
  by_sentiment: {
    [key: string]: {
      count: number;
      avg_confidence: number;
      avg_processing_time: number;
    };
  };
  by_date: Array<{
    date: string;
    total: number;
    positive: number;
    negative: number;
  }>;
  confidence_distribution: {
    high: number;
    medium: number;
    low: number;
  };
  avg_processing_time: number;
  recent_trends: Array<{
    hour: string;
    count: number;
  }>;
}

export const mlApi = api.injectEndpoints({
  endpoints: (builder) => ({
    predictSentiment: builder.mutation<PredictionResult, { text: string }>({
      query: (body) => ({
        url: "/ml/predict",
        method: "POST",
        body,
      }),
      invalidatesTags: ["ML", "MLHistory", "MLStats"],
    }),
    getModelInfo: builder.query<ModelInfo, void>({
      query: () => "/ml/model-info",
    }),
    getPredictionHistory: builder.query<
      PredictionHistoryResponse,
      { page?: number; pageSize?: number; sentiment?: string }
    >({
      query: ({ page = 1, pageSize = 10, sentiment }) => {
        const skip = (page - 1) * pageSize;
        const params = new URLSearchParams({
          skip: skip.toString(),
          limit: pageSize.toString(),
        });
        if (sentiment) {
          params.append("sentiment", sentiment);
        }
        return `/ml/history?${params.toString()}`;
      },
      providesTags: ["MLHistory"],
    }),
    getMLStats: builder.query<MLStatsResponse, void>({
      query: () => "/ml/stats",
      providesTags: ["MLStats"],
    }),
  }),
});

export const {
  usePredictSentimentMutation,
  useGetModelInfoQuery,
  useGetPredictionHistoryQuery,
  useGetMLStatsQuery,
} = mlApi;
