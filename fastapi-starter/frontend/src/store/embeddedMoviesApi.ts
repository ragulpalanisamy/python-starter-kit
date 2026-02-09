import { api } from "./api";
import type { EmbeddedMovie, PaginatedResponse } from "../types";

export const embeddedMoviesApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getEmbeddedMovies: builder.query<PaginatedResponse<EmbeddedMovie>, { page: number; pageSize: number }>({
      query: ({ page, pageSize }) => `/embedded-movies?page=${page}&page_size=${pageSize}`,
      providesTags: ["EmbeddedMovies"],
    }),
    getEmbeddedMovieById: builder.query<EmbeddedMovie, string>({
      query: (id) => `/embedded-movies/${id}`,
      providesTags: (_result, _error, id) => [{ type: "EmbeddedMovies", id }],
    }),
    createEmbeddedMovie: builder.mutation<EmbeddedMovie, Partial<EmbeddedMovie>>({
      query: (body) => ({
        url: "/embedded-movies",
        method: "POST",
        body,
      }),
      invalidatesTags: ["EmbeddedMovies"],
    }),
    updateEmbeddedMovie: builder.mutation<EmbeddedMovie, { id: string; body: Partial<EmbeddedMovie> }>({
      query: ({ id, body }) => ({
        url: `/embedded-movies/${id}`,
        method: "PUT",
        body,
      }),
      invalidatesTags: (_result, _error, { id }) => ["EmbeddedMovies", { type: "EmbeddedMovies", id }],
    }),
    deleteEmbeddedMovie: builder.mutation<void, string>({
      query: (id) => ({
        url: `/embedded-movies/${id}`,
        method: "DELETE",
      }),
      invalidatesTags: ["EmbeddedMovies"],
    }),
  }),
});

export const {
  useGetEmbeddedMoviesQuery,
  useGetEmbeddedMovieByIdQuery,
  useCreateEmbeddedMovieMutation,
  useUpdateEmbeddedMovieMutation,
  useDeleteEmbeddedMovieMutation,
} = embeddedMoviesApi;
