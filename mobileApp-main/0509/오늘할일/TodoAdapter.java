package com.example.todolist;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.todolist.TodoItem;

import java.util.ArrayList;

public class TodoAdapter extends RecyclerView.Adapter<TodoAdapter.TodoViewHolder> {
    private ArrayList<TodoItem> todoList;

    public TodoAdapter(ArrayList<TodoItem> todoList) {
        this.todoList = todoList;
    }

    public static class TodoViewHolder extends RecyclerView.ViewHolder {
        CheckBox checkBox;
        TextView titleText;
        ImageButton deleteButton;

        public TodoViewHolder(View itemView) {
            super(itemView);
            checkBox = itemView.findViewById(R.id.todo_checkbox);
            titleText = itemView.findViewById(R.id.todo_title);
            deleteButton = itemView.findViewById(R.id.delete_button);
        }
    }

    @NonNull
    @Override
    public TodoViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_todo, parent, false);
        return new TodoViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull TodoViewHolder holder, int position) {
        TodoItem item = todoList.get(position);
        holder.titleText.setText(item.getTitle());
        holder.checkBox.setChecked(item.isDone());

        holder.checkBox.setOnCheckedChangeListener((buttonView, isChecked) -> {
            item.setDone(isChecked);
        });

        holder.deleteButton.setOnClickListener(v -> {
            todoList.remove(position);
            notifyItemRemoved(position);
            notifyItemRangeChanged(position, todoList.size());
        });
    }

    @Override
    public int getItemCount() {
        return todoList.size();
    }
}
