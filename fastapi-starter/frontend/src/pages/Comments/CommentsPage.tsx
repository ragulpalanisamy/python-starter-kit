import { Card, CardBody } from "@heroui/react";
import { Calendar, User as UserIcon, MessageSquare } from "lucide-react";
import { useState } from "react";
import { useGetCommentsQuery } from "../../store/commentsApi";
import { PageHeader, LoadingSpinner, RefetchButton, Pagination } from "../../components/shared";
import { PAGE_SIZES } from "../../constants";

export const CommentsPage = () => {
  const [page, setPage] = useState(1);
  const { data, isLoading, isFetching, refetch } = useGetCommentsQuery({
    page,
    pageSize: PAGE_SIZES.COMMENTS,
  });

  return (
    <div className="space-y-2">
      <PageHeader
        title="Community Reviews"
        description="Real-time audience feedback and discussions"
        action={<RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />}
      />

      <Card className="bg-white/5 border-slate-700/20 backdrop-blur-xl shadow-2xl overflow-hidden rounded-lg">
        <CardBody className="p-2 relative min-h-[400px]">
          <div className={isFetching || isLoading ? "opacity-50 pointer-events-none" : ""}>
            {isLoading || isFetching ? (
              <div className="flex items-center justify-center py-16">
                <LoadingSpinner size="lg" label="Loading reviews..." />
              </div>
            ) : data?.items.length === 0 ? (
              <div className="text-center py-16 opacity-30 flex flex-col items-center gap-2">
                <MessageSquare size={48} className="text-white" />
                <p className="text-sm font-bold uppercase tracking-wide text-white">No Reviews Found</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
                {(data?.items || []).map((comment, index) => (
                  <div
                    key={comment.id}
                    className={`bg-white/5 border border-slate-700/20 rounded-lg p-2 hover:bg-white/10 hover:border-slate-600/30 transition-all group ${index > 0 ? "mt-1" : ""}`}
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <div className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center border border-slate-600/20 shrink-0 group-hover:bg-white/20 transition-all">
                        <UserIcon size={16} className="text-white" />
                      </div>
                      <div className="min-w-0 flex-1">
                        <p className="font-semibold text-white text-sm truncate">{comment.name}</p>
                        <p className="text-[9px] text-slate-400 lowercase font-medium truncate">
                          {comment.email}
                        </p>
                      </div>
                    </div>

                    <div className="p-2 bg-white/5 border border-slate-700/20 rounded-lg mb-2 backdrop-blur-sm">
                      <p className="text-xs text-slate-300 leading-relaxed italic line-clamp-3">
                        "{comment.text}"
                      </p>
                    </div>

                    <div className="flex items-center gap-1.5 text-slate-400 text-[10px] font-mono">
                      <Calendar size={10} />
                      {new Date(comment.date).toLocaleDateString()}
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
