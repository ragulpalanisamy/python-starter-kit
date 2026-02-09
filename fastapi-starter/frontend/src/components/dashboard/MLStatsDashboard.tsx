import { Card, CardBody, CardHeader, Select, SelectItem } from "@heroui/react";
import dayjs from "dayjs";
import { entries } from "lodash";
import { Activity, Clock, Target, TrendingUp } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Legend,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import type { MLStatsResponse } from "../../store/mlApi";
import { Chip, LoadingSpinner, RefetchButton } from "../shared";

const COLORS = {
  positive: "#22c55e",
  negative: "#ef4444",
  neutral: "#64748b",
  high: "#22c55e",
  medium: "#eab308",
  low: "#ef4444",
};

const CHART_COLORS = {
  background: "rgba(255, 255, 255, 0.05)",
  grid: "rgba(148, 163, 184, 0.1)",
  text: "#e2e8f0",
  border: "rgba(148, 163, 184, 0.2)",
};

interface MLStatsDashboardProps {
  stats: MLStatsResponse | undefined;
  isLoading: boolean;
  isFetching: boolean;
  error: unknown;
  onRefetch: () => void;
}

export const MLStatsDashboard = ({ stats, isLoading, isFetching, error, onRefetch }: MLStatsDashboardProps) => {
  console.log("🚀 MLStatsDashboard - Function component executing");
  console.log("🚀 MLStatsDashboard - Props:", { isLoading, isFetching, hasError: !!error, hasData: !!stats });
  
  const [timeRange, setTimeRange] = useState("30d");
  
  useEffect(() => {
    console.log("MLStatsDashboard - Component mounted");
    console.log("MLStatsDashboard - Props state:", { isLoading, isFetching, error, hasData: !!stats });
    return () => {
      console.log("MLStatsDashboard - Component unmounting");
    };
  }, [isLoading, isFetching, error, stats]);

  // Memoize chart data to prevent unnecessary recalculations
  const sentimentData = useMemo(() => {
    if (!stats?.by_sentiment) return [];
    return entries(stats.by_sentiment).map(([name, value]) => ({
      name,
      count: value.count,
      avgConfidence: (value.avg_confidence * 100).toFixed(1),
      avgProcessingTime: value.avg_processing_time,
    }));
  }, [stats?.by_sentiment]);

  const pieData = useMemo(() => {
    if (!stats?.by_sentiment) return [];
    return entries(stats.by_sentiment).map(([name, value]) => ({
      name,
      value: value.count,
    }));
  }, [stats?.by_sentiment]);

  const confidenceData = useMemo(() => {
    if (!stats?.confidence_distribution) return [];
    const { high, medium, low } = stats.confidence_distribution;
    return [
      { name: "High (≥80%)", value: high, color: COLORS.high },
      { name: "Medium (50-80%)", value: medium, color: COLORS.medium },
      { name: "Low (<50%)", value: low, color: COLORS.low },
    ];
  }, [stats?.confidence_distribution]);

  const dateData = useMemo(() => {
    if (!stats?.by_date?.length) return [];
    const daysMap: Record<string, number> = { "7d": 7, "14d": 14, "30d": 30 };
    const days = daysMap[timeRange] || 30;
    return stats.by_date.slice(-days).map((item) => ({
      ...item,
      date: dayjs(item.date).format("MMM DD"), // Format dates nicely
    }));
  }, [stats?.by_date, timeRange]);

  const recentTrendsData = useMemo(() => {
    if (!stats?.recent_trends?.length) return [];
    return stats.recent_trends.map((item) => ({
      ...item,
      hour: dayjs(item.hour).format("HH:mm"), // Format hour nicely
    }));
  }, [stats?.recent_trends]);

  if (isLoading) {
    return (
      <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
        <CardBody className="flex items-center justify-center min-h-[400px]">
          <LoadingSpinner size="lg" label="Loading statistics..." />
        </CardBody>
      </Card>
    );
  }

  if (error) {
    return (
      <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
        <CardBody className="flex flex-col items-center justify-center min-h-[400px] gap-2">
          <p className="text-red-400 font-semibold">Failed to load statistics</p>
          <button
            onClick={onRefetch}
            className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-white text-sm transition-colors"
          >
            Retry
          </button>
        </CardBody>
      </Card>
    );
  }

  if (!stats) {
    console.log("MLStatsDashboard - No stats data, returning null");
    return null;
  }
  
  console.log("MLStatsDashboard - Rendering dashboard with stats");

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-slate-950/95 border border-slate-700/20 p-2 rounded-lg backdrop-blur-xl shadow-lg">
          {label && <p className="text-[10px] font-semibold text-slate-400 mb-1 uppercase">{label}</p>}
          {payload.map((entry: any, index: number) => (
            <p key={index} className="text-xs text-white flex items-center gap-2">
              <span
                className="w-2 h-2 rounded-full"
                style={{ backgroundColor: entry.color }}
              />
              <span>{entry.name}:</span>
              <span className="font-bold" style={{ color: entry.color }}>
                {typeof entry.value === "number" ? entry.value.toLocaleString() : entry.value}
              </span>
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="space-y-2">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-2">
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl rounded-lg">
          <CardBody className="p-3">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[9px] text-slate-400 font-semibold uppercase tracking-wide">Total Predictions</p>
                <p className="text-2xl font-bold text-white mt-1">{stats.total}</p>
              </div>
              <div className="bg-white/10 p-2 rounded-lg border border-slate-600/20">
                <Activity className="text-white" size={20} />
              </div>
            </div>
          </CardBody>
        </Card>

        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl rounded-lg">
          <CardBody className="p-3">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[9px] text-slate-400 font-semibold uppercase tracking-wide">Avg Processing Time</p>
                <p className="text-2xl font-bold text-white mt-1">{stats.avg_processing_time}ms</p>
              </div>
              <div className="bg-white/10 p-2 rounded-lg border border-slate-600/20">
                <Clock className="text-white" size={20} />
              </div>
            </div>
          </CardBody>
        </Card>

        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl rounded-lg">
          <CardBody className="p-3">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[9px] text-slate-400 font-semibold uppercase tracking-wide">Positive</p>
                <p className="text-2xl font-bold text-white mt-1">
                  {stats.by_sentiment.POSITIVE?.count || 0}
                </p>
              </div>
              <div className="bg-green-500/20 p-2 rounded-lg border border-green-500/30">
                <TrendingUp className="text-green-400" size={20} />
              </div>
            </div>
          </CardBody>
        </Card>

        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl rounded-lg">
          <CardBody className="p-3">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[9px] text-slate-400 font-semibold uppercase tracking-wide">Negative</p>
                <p className="text-2xl font-bold text-white mt-1">
                  {stats.by_sentiment.NEGATIVE?.count || 0}
                </p>
              </div>
              <div className="bg-red-500/20 p-2 rounded-lg border border-red-500/30">
                <Target className="text-red-400" size={20} />
              </div>
            </div>
          </CardBody>
        </Card>
      </div>

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-2">
        {/* Sentiment Distribution Pie Chart */}
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
            <div className="flex gap-2 items-center">
              <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
                <Activity className="text-white" size={16} />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Sentiment Distribution</p>
                <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase">
                  Overall Breakdown
                </p>
              </div>
            </div>
            <RefetchButton onRefetch={onRefetch} isFetching={isFetching} />
          </CardHeader>
          <CardBody className="p-2">
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={(props: any) => {
                    const name = props.name ?? "Unknown";
                    const percent = props.percent ?? 0;
                    return `${name}: ${(percent * 100).toFixed(0)}%`;
                  }}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                  stroke={CHART_COLORS.border}
                  strokeWidth={2}
                >
                  {pieData.map((entry, index) => (
                    <Cell
                      key={`cell-${index}`}
                      fill={entry.name === "POSITIVE" ? COLORS.positive : COLORS.negative}
                    />
                  ))}
                </Pie>
                <Tooltip content={<CustomTooltip />} />
                <Legend
                  wrapperStyle={{ color: CHART_COLORS.text, fontSize: "10px" }}
                  iconType="circle"
                />
              </PieChart>
            </ResponsiveContainer>
          </CardBody>
        </Card>

        {/* Confidence Distribution */}
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
            <div className="flex gap-2 items-center">
              <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
                <Target className="text-white" size={16} />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Confidence Distribution</p>
                <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase">
                  Prediction Quality
                </p>
              </div>
            </div>
          </CardHeader>
          <CardBody className="p-2">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={confidenceData}>
                <CartesianGrid strokeDasharray="3 3" stroke={CHART_COLORS.grid} />
                <XAxis
                  dataKey="name"
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <YAxis
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <Tooltip content={<CustomTooltip />} />
                <Bar dataKey="value" radius={[8, 8, 0, 0]}>
                  {confidenceData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </CardBody>
        </Card>

        {/* Sentiment Counts Bar Chart */}
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
            <div className="flex gap-2 items-center">
              <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
                <TrendingUp className="text-white" size={16} />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Sentiment Comparison</p>
                <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase">
                  Count & Confidence
                </p>
              </div>
            </div>
          </CardHeader>
          <CardBody className="p-2">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={sentimentData}>
                <CartesianGrid strokeDasharray="3 3" stroke={CHART_COLORS.grid} />
                <XAxis
                  dataKey="name"
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <YAxis
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <Tooltip content={<CustomTooltip />} />
                <Legend
                  wrapperStyle={{ color: CHART_COLORS.text, fontSize: "10px" }}
                  iconType="square"
                />
                <Bar dataKey="count" radius={[8, 8, 0, 0]}>
                  {sentimentData.map((entry, index) => (
                    <Cell
                      key={`cell-${index}`}
                      fill={entry.name === "POSITIVE" ? COLORS.positive : COLORS.negative}
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-2 flex gap-2 justify-center">
              {sentimentData.map((item) => (
                <Chip key={item.name} size="sm" variant="flat" className="text-[8px]">
                  {item.name}: {item.avgConfidence}% avg confidence
                </Chip>
              ))}
            </div>
          </CardBody>
        </Card>

        {/* Time Series Chart */}
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
            <div className="flex gap-2 items-center">
              <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
                <Clock className="text-white" size={16} />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Prediction Trends</p>
                <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase">
                  Over Time
                </p>
              </div>
            </div>
            <Select
              size="sm"
              selectedKeys={[timeRange]}
              onSelectionChange={(keys) => {
                const selected = Array.from(keys)[0];
                if (selected) setTimeRange(selected as string);
              }}
              className="max-w-[120px]"
              classNames={{
                trigger: "bg-white/10 border-slate-600/20 text-white",
                popoverContent: "bg-slate-950 border-slate-700/20",
              }}
            >
              <SelectItem key="7d">7 Days</SelectItem>
              <SelectItem key="14d">14 Days</SelectItem>
              <SelectItem key="30d">30 Days</SelectItem>
            </Select>
          </CardHeader>
          <CardBody className="p-2">
            <ResponsiveContainer width="100%" height={300}>
              <AreaChart data={dateData}>
                <defs>
                  <linearGradient id="colorPositive" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor={COLORS.positive} stopOpacity={0.8} />
                    <stop offset="95%" stopColor={COLORS.positive} stopOpacity={0} />
                  </linearGradient>
                  <linearGradient id="colorNegative" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor={COLORS.negative} stopOpacity={0.8} />
                    <stop offset="95%" stopColor={COLORS.negative} stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke={CHART_COLORS.grid} />
                <XAxis
                  dataKey="date"
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  angle={-45}
                  textAnchor="end"
                  height={60}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <YAxis
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <Tooltip content={<CustomTooltip />} />
                <Legend
                  wrapperStyle={{ color: CHART_COLORS.text, fontSize: "10px" }}
                  iconType="square"
                />
                <Area
                  type="monotone"
                  dataKey="positive"
                  stroke={COLORS.positive}
                  fillOpacity={1}
                  fill="url(#colorPositive)"
                />
                <Area
                  type="monotone"
                  dataKey="negative"
                  stroke={COLORS.negative}
                  fillOpacity={1}
                  fill="url(#colorNegative)"
                />
              </AreaChart>
            </ResponsiveContainer>
          </CardBody>
        </Card>
      </div>

      {/* Recent Trends */}
      {recentTrendsData.length > 0 && (
        <Card className="bg-white/5 border border-slate-700/20 backdrop-blur-xl shadow-2xl rounded-lg">
          <CardHeader className="flex justify-between items-center p-2 gap-1 border-b border-slate-700/20">
            <div className="flex gap-2 items-center">
              <div className="bg-white/10 p-1 rounded-lg shrink-0 border border-slate-600/20">
                <Activity className="text-white" size={16} />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Recent Activity</p>
                <p className="text-[9px] text-slate-400 font-semibold tracking-wide uppercase">
                  Last 24 Hours
                </p>
              </div>
            </div>
          </CardHeader>
          <CardBody className="p-2">
            <ResponsiveContainer width="100%" height={250}>
              <LineChart data={recentTrendsData}>
                <CartesianGrid strokeDasharray="3 3" stroke={CHART_COLORS.grid} />
                <XAxis
                  dataKey="hour"
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  angle={-45}
                  textAnchor="end"
                  height={60}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <YAxis
                  stroke={CHART_COLORS.text}
                  fontSize={10}
                  tick={{ fill: CHART_COLORS.text }}
                />
                <Tooltip content={<CustomTooltip />} />
                <Line
                  type="monotone"
                  dataKey="count"
                  stroke={COLORS.positive}
                  strokeWidth={2}
                  dot={{ fill: COLORS.positive, r: 4 }}
                  activeDot={{ r: 6 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </CardBody>
        </Card>
      )}
    </div>
  );
};
