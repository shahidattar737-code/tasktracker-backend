function TaskItem({ task, onToggle, onDelete }) {
  return (
    <div className={`task-item ${task.completed ? "completed" : ""}`}>
      <label className="task-content">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggle(task.id)}
        />

        <span>{task.text}</span>
      </label>

      <button
        className="delete-btn"
        onClick={() => onDelete(task.id)}
      >
        Delete
      </button>
    </div>
  );
}

export default TaskItem;