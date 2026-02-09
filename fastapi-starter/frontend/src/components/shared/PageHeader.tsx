import type { ReactNode } from "react";

interface PageHeaderProps {
  title: string;
  description?: string;
  action?: ReactNode;
  icon?: ReactNode;
}

export const PageHeader = ({ title, description, action, icon }: PageHeaderProps) => {
  return (
    <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-2">
      <div className="flex items-start gap-2">
        {icon && <div className="mt-1">{icon}</div>}
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold text-white">{title}</h1>
          {description && <p className="text-sm text-slate-400 mt-1">{description}</p>}
        </div>
      </div>
      {action && <div>{action}</div>}
    </div>
  );
};
