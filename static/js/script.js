function createSubjectFields() {

    const subjectCount = document.getElementById("subjects").value;
    const container = document.getElementById("subject-container");

    container.innerHTML = "";

    for (let i = 1; i <= subjectCount; i++) {

        const subjectBox = document.createElement("div");

        subjectBox.className = "subject-box";

        subjectBox.innerHTML = `
            <h3>Subject ${i}</h3>

            <div class="form-group">
                <label>Subject Name</label>
                <input 
                    type="text"
                    name="subject_name_${i}"
                    placeholder="Enter subject name"
                    required
                >
            </div>

            <div class="form-group">
                <label>Internal Marks</label>
                <input 
                    type="number"
                    name="internal_marks_${i}"
                    min="0"
                    max="100"
                    placeholder="Enter internal marks"
                    required
                >
            </div>
        `;

        container.appendChild(subjectBox);
    }
}
