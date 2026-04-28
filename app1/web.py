import streamlit as st
import modules.functions as functions

def add_todo():
    inp_value = st.session_state["new_todo"]
    todos.append(inp_value + '\n')
    functions.write_todos(todos)


def complete_todo():
    inp_value = st.session_state["new_todo"]

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("My Todos")
st.text("Bla bla bla text")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


# streamlit run web.pyc