import type { TodoFilter } from './api'

export const todoKeys = {
  all: ['todos'] as const,
  lists: () => [...todoKeys.all, 'list'] as const,
  list: (filter: TodoFilter) => [...todoKeys.lists(), filter] as const,
}