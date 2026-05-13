import { useQuery } from '@tanstack/react-query'
import { getTodos } from '../api'
import { todoKeys } from '../todoKeys'

export function useTodosQuery() {
  return useQuery({
    queryKey: todoKeys.all,
    queryFn: () => getTodos(),
  })
}