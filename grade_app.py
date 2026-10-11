import streamlit as st


def get_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"


st.title("Student Grade Manager")


# Create session state
if "students" not in st.session_state:
    st.session_state.students = []


# Form
with st.form("add"):

    name = st.text_input("Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add")

    if submitted:

        if name.strip():

            grade = get_grade(mark)

            st.session_state.students.append({
                "Name": name,
                "Mark": mark,
                "Grade": grade
            })

            st.success(
                f"Added {name} with mark {mark}"
            )

        else:
            st.error("Please enter student name")


# Display results
if st.session_state.students:

    st.subheader("Student Results")

    # IMPORTANT:
    # Do not use st.table(...)
    st.table(st.session_state.students)


    # Get all marks
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)


    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average",
        f"{average:.1f}"
    )

    col2.metric(
        "Highest",
        highest
    )

    col3.metric(
        "Lowest",
        lowest
    )

else:

    st.info("No students added yet.")