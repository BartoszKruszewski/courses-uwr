import { useMutation, useQueryClient } from '@tanstack/react-query'
import { deleteTodo } from '../api'
import { todoKeys } from '../todoKeys'

export function useDeleteTodoMutation() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: deleteTodo,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: todoKeys.all })
    },
  })
}