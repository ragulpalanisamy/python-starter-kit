import { api } from "./api";
import type { Theater, PaginatedResponse } from "../types";

export const theatersApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getTheaters: builder.query<PaginatedResponse<Theater>, { page: number; pageSize: number }>({
      query: ({ page, pageSize }) => `/theaters?page=${page}&page_size=${pageSize}`,
      providesTags: ["Theaters"],
    }),
    getTheaterById: builder.query<Theater, string>({
      query: (id) => `/theaters/${id}`,
      providesTags: (_result, _error, id) => [{ type: "Theaters", id }],
    }),
    createTheater: builder.mutation<Theater, Partial<Theater>>({
      query: (body) => ({
        url: "/theaters",
        method: "POST",
        body,
      }),
      invalidatesTags: ["Theaters"],
    }),
    updateTheater: builder.mutation<Theater, { id: string; body: Partial<Theater> }>({
      query: ({ id, body }) => ({
        url: `/theaters/${id}`,
        method: "PUT",
        body,
      }),
      invalidatesTags: (_result, _error, { id }) => ["Theaters", { type: "Theaters", id }],
    }),
    deleteTheater: builder.mutation<void, string>({
      query: (id) => ({
        url: `/theaters/${id}`,
        method: "DELETE",
      }),
      invalidatesTags: ["Theaters"],
    }),
  }),
});

export const {
  useGetTheatersQuery,
  useGetTheaterByIdQuery,
  useCreateTheaterMutation,
  useUpdateTheaterMutation,
  useDeleteTheaterMutation,
} = theatersApi;
