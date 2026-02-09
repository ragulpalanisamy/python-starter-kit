import { api } from "./api";
import type { Comment, PaginatedResponse } from "../types";

export const commentsApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getComments: builder.query<PaginatedResponse<Comment>, { page: number; pageSize: number }>({
      query: ({ page, pageSize }) => `/comments?page=${page}&page_size=${pageSize}`,
      providesTags: ["Comments"],
    }),
    getCommentById: builder.query<Comment, string>({
      query: (id) => `/comments/${id}`,
      providesTags: (_result, _error, id) => [{ type: "Comments", id }],
    }),
    createComment: builder.mutation<Comment, Partial<Comment>>({
      query: (body) => ({
        url: "/comments",
        method: "POST",
        body,
      }),
      invalidatesTags: ["Comments"],
    }),
    updateComment: builder.mutation<Comment, { id: string; body: Partial<Comment> }>({
      query: ({ id, body }) => ({
        url: `/comments/${id}`,
        method: "PUT",
        body,
      }),
      invalidatesTags: (_result, _error, { id }) => ["Comments", { type: "Comments", id }],
    }),
    deleteComment: builder.mutation<void, string>({
      query: (id) => ({
        url: `/comments/${id}`,
        method: "DELETE",
      }),
      invalidatesTags: ["Comments"],
    }),
  }),
});

export const {
  useGetCommentsQuery,
  useGetCommentByIdQuery,
  useCreateCommentMutation,
  useUpdateCommentMutation,
  useDeleteCommentMutation,
} = commentsApi;
