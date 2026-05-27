"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { submitTodo } from "./lib/api";

export async function createTodo(formData: FormData) {
  const text = formData.get("text")?.toString() || "";
  await submitTodo({ text, done: false }, "POST");

  revalidatePath("/todos");
  redirect("/todos");
}

export async function updateTodo(id: string, formData: FormData) {
  const text = formData.get("text")?.toString() || "";
  const done = formData.get("done") === "on";
  await submitTodo({ text, done }, "PUT", id);

  revalidatePath("/todos");
  redirect("/todos");
}

export async function toggleTodoStatus(id: string, text: string, currentDone: boolean) {
  await submitTodo({ text, done: !currentDone }, "PUT", id);
  revalidatePath("/todos");
}
