import { Beaker } from "lucide-react";
import type { ModelInfo } from "../../types";

interface HeaderProps {
  modelInfo?: ModelInfo;
}

export const Header = ({ modelInfo }: HeaderProps) => {
  return (
    <header className="mb-2 flex flex-col sm:flex-row sm:items-center justify-end gap-2">
    
      {modelInfo && (
        <div className="bg-white/5 backdrop-blur-sm border border-slate-700/20 rounded-xl p-2 flex items-center gap-2 hover:border-slate-600/30 transition-colors group shrink-0">
          <div className="bg-white/10 p-1 rounded-lg group-hover:scale-110 transition-transform shrink-0">
            <Beaker className="text-white" size={16} />
          </div>
          <div className="min-w-0">
            <p className="text-[9px] text-slate-400 uppercase font-bold tracking-tight">Model</p>
            <p className="text-xs sm:text-sm font-semibold text-white truncate">
              {modelInfo.model_name.split("/").pop()}
            </p>
          </div>
        </div>
      )}
    </header>
  );
};
