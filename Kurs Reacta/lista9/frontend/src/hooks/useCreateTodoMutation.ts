import { useMutation, useQueryClient } from '@tanstack/react-query'
import { createTodo } from '../api'
import { todoKeys } from '../todoKeys'

export function useCreateTodoMutation() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: createTodo,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: todoKeys.all })
    },
  })
}