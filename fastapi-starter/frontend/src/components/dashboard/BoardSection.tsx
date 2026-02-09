import { useState, useMemo } from "react";
import { Card, CardBody, CardHeader, ScrollShadow, Divider } from "@heroui/react";
import { Layout, Plus, Database, AlertCircle, Hash, SortAsc, SortDesc } from "lucide-react";
import { useGetBoardsQuery, useCreateBoardMutation } from "../../store/api";
import { toast } from "react-hot-toast";
import type { Board } from "../../types";
import { FormField, LoadingSpinner, RefetchButton, SkeletonLoader, Button, Chip } from "../shared";

export const BoardSection = () => {
  const [boardName, setBoardName] = useState("");
  const [sortOrder, setSortOrder] = useState<"asc" | "desc">("desc");

  const {
    data: boards,
    isLoading: boardsLoading,
    error: boardsError,
    isFetching,
    refetch,
  } = useGetBoardsQuery();
  const [createBoard] = useCreateBoardMutation();

  const sortedBoards = useMemo(() => {
    if (!boards) return [];
    return [...boards].sort((a, b) => {
      const comparison = a.name.localeCompare(b.name, undefined, {
        numeric: true,
        sensitivity: 'base'
      });
      return sortOrder === "asc" ? comparison : -comparison;
    });
  }, [boards, sortOrder]);

  const handleCreateBoard = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!boardName.trim()) return;

    const boardId = Math.floor(Math.random() * 1000000);
    try {
      await createBoard({
        board_id: boardId,
        name: boardName,
        status: "ACTIVE",
      }).unwrap();
      setBoardName("");
      toast.success("Board indexed successfully");
    } catch {
      toast.error("Database persistence failed");
    }
  };

  return (
    <Card className="bg-linear-to-br from-cyan-500/10 to-teal-500/10 border-2 border-cyan-500/30 backdrop-blur-xl h-full shadow-2xl transition-all duration-300 hover:border-cyan-500/50 hover:shadow-cyan-500/20 rounded-lg">
      <CardHeader className="flex gap-2 p-2 border-b border-cyan-500/20 bg-linear-to-r from-cyan-500/5 to-transparent">
        <div className="bg-linear-to-br from-cyan-500/30 to-teal-500/30 p-1 rounded-lg shadow-lg transition-transform duration-200 hover:scale-105 ring-2 ring-cyan-500/20">
          <Layout className="text-white" size={16} />
        </div>
        <div className="min-w-0 flex-1">
          <p className="text-sm font-bold truncate bg-linear-to-r from-cyan-300 to-teal-300 bg-clip-text text-transparent">
            Data Explorer
          </p>
          <p className="text-[9px] text-cyan-300/80 font-semibold tracking-wide uppercase truncate">
            MongoDB Persistence
          </p>
        </div>

        <div className="flex items-center gap-1">
          <Button
            isIconOnly
            size="sm"
            variant="light"
            className="text-cyan-300 hover:bg-cyan-500/20"
            onClick={() => setSortOrder(prev => prev === "asc" ? "desc" : "asc")}
            title={`Sort ${sortOrder === "asc" ? "Descending" : "Ascending"}`}
          >
            {sortOrder === "asc" ? <SortAsc size={16} /> : <SortDesc size={16} />}
          </Button>

          <RefetchButton onRefetch={() => refetch()} isFetching={isFetching} />
        </div>
      </CardHeader>

      <CardBody className="px-2 pb-2 pt-2 flex flex-col h-full">
        <form onSubmit={handleCreateBoard} className="mb-2">
          <div className="flex gap-1 items-end">
            <div className="flex-1 min-w-0">
              <FormField
                type="input"
                label="Board Name"
                value={boardName}
                onChange={setBoardName}
                placeholder="New board instance..."
              />
            </div>
            <Button
              type="submit"
              isIconOnly
              isDisabled={!boardName.trim()}
              size="md"
              className="bg-white/10 hover:bg-white/20 text-white border border-white/10"
            >
              <Plus size={16} />
            </Button>
          </div>
        </form>

        <Divider className="mb-2 opacity-25" />

        <ScrollShadow className="flex-1 max-h-[300px] min-h-[200px] overflow-y-auto pr-1 [&::-webkit-scrollbar]:w-1 [&::-webkit-scrollbar-thumb]:bg-cyan-500/30 [&::-webkit-scrollbar-thumb]:rounded-full hover:[&::-webkit-scrollbar-thumb]:bg-cyan-500/50">
          <div className="relative min-h-[200px]">
            {isFetching && (
              <div className="absolute inset-0 flex items-center justify-center bg-slate-950/30 backdrop-blur-sm rounded-lg z-10">
                <LoadingSpinner size="sm" />
              </div>
            )}
            <div className={`space-y-1 pr-2 ${isFetching ? "opacity-50 pointer-events-none" : ""}`}>
              {boardsLoading ? (
                <SkeletonLoader count={3} variant="card" />
              ) : boardsError ? (
                <div className="bg-white/5 border border-slate-700/20 p-2 rounded-lg flex flex-col items-center gap-2 backdrop-blur-sm">
                  <AlertCircle className="text-white" size={20} />
                  <p className="text-white text-center text-xs font-semibold leading-tight">
                    CONNECTION FAILED
                    <br />
                    <span className="text-[9px] opacity-60">VERIFY MONGODB CONNECTIVITY</span>
                  </p>
                </div>
              ) : boards?.length === 0 ? (
                <div className="text-center py-10 opacity-30 flex flex-col items-center gap-2">
                  <Database size={32} className="text-white" />
                  <p className="text-[9px] font-bold uppercase tracking-wide text-white">No Records</p>
                </div>
              ) : (
                sortedBoards.map((board: Board, index) => (
                  <div
                    key={board.board_id}
                    className={`bg-white/5 border border-slate-700/20 p-2 rounded-lg flex justify-between items-center group hover:bg-white/10 hover:border-slate-600/30 transition-all gap-1 ${index > 0 ? "mt-1" : ""}`}
                  >
                    <div className="flex items-center gap-2 min-w-0 flex-1">
                      <div className="bg-white/10 h-8 w-8 rounded-lg flex items-center justify-center border border-slate-600/20 group-hover:bg-white/20 transition-all shrink-0">
                        <Hash size={12} className="text-white" />
                      </div>
                      <div className="min-w-0 flex-1">
                        <h3 className="font-semibold text-white text-sm truncate">{board.name}</h3>
                        <p className="text-[9px] font-mono text-slate-400 truncate">ID: {board.board_id}</p>
                      </div>
                    </div>
                    <Chip variant="flat" size="sm" className="font-bold text-[8px] uppercase">
                      {board.status}
                    </Chip>
                  </div>
                ))
              )}
            </div>
          </div>
        </ScrollShadow>
      </CardBody>
    </Card >
  );
};
