import { motion } from "framer-motion";
import { BoardSection } from "../../components/dashboard/BoardSection";
import { HistorySection } from "../../components/dashboard/HistorySection";
import { SentimentSection } from "../../components/dashboard/SentimentSection";
import { MLStatsDashboard } from "../../components/dashboard/MLStatsDashboard";
import { Header } from "../../components/layout/Header";
import { useGetModelInfoQuery, useGetMLStatsQuery } from "../../store/mlApi";

export const DashboardPage = () => {
  const { data: modelInfo } = useGetModelInfoQuery();
  const { data: stats, isLoading: statsLoading, isFetching: statsFetching, refetch: refetchStats, error: statsError } = useGetMLStatsQuery(undefined, {
    refetchOnMountOrArgChange: true,
  });

  return (
    <>
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="mb-2"
      >
        <Header modelInfo={modelInfo} />
      </motion.div>
      <div className="space-y-2">
        <main className="grid grid-cols-1 lg:grid-cols-2 gap-2 items-stretch">
          <motion.section
            className="h-full"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
          >
            <SentimentSection />
          </motion.section>

          <motion.section
            className="h-full"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <BoardSection />
          </motion.section>
        </main>

        <motion.section
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-2"
        >
          <MLStatsDashboard
            stats={stats}
            isLoading={statsLoading}
            isFetching={statsFetching}
            error={statsError}
            onRefetch={refetchStats}
          />
        </motion.section>

        <motion.section
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-2"
        >
          <HistorySection />
        </motion.section>
      </div>
    </>
  );
};
