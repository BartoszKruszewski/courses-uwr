import { useMutation, useQueryClient } from '@tanstack/react-query'
import { updateTodo, type UpdateTodoInput } from '../api'
import { todoKeys } from '../todoKeys'

type UpdateTodoVariables = {
  id: string
  todo: UpdateTodoInput
}

export function useUpdateTodoMutation() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, todo }: UpdateTodoVariables) => updateTodo(id, todo),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: todoKeys.all })
    },
  })
}