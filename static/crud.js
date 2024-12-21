function showForm() {
    const operation = document.querySelector('input[name="operation"]:checked').value;
    const entity = document.querySelector('input[name="entity"]:checked').value;
    const formContainer = document.getElementById('form-container');
    formContainer.innerHTML = '';

    if (operation === 'search') {
        formContainer.innerHTML = `
            <div class="form-group">
                <label for="search">Search ${entity}:</label>
                <input type="text" id="search" name="search" required>
            </div>
        `;
    } else if (operation === 'add') {
        if (entity === 'user') {
            formContainer.innerHTML = `
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div class="form-group">
                    <label for="pay_info">Payment Info:</label>
                    <input type="text" id="pay_info" name="pay_info">
                </div>
                <div class="form-group">
                    <label for="balance">Balance:</label>
                    <input type="number" step="0.01" id="balance" name="balance">
                </div>
            `;
        } else if (entity === 'developer') {
            formContainer.innerHTML = `
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div class="form-group">
                    <label for="contact_info">Contact Info:</label>
                    <input type="text" id="contact_info" name="contact_info">
                </div>
                <div class="form-group">
                    <label for="website">Website:</label>
                    <input type="url" id="website" name="website">
                </div>
            `;
        } else if (entity === 'app') {
            formContainer.innerHTML = `
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="app_version">App Version:</label>
                    <input type="number" step="0.001" id="app_version" name="app_version" required>
                </div>
                <div class="form-group">
                    <label for="price">Price:</label>
                    <input type="number" step="0.01" id="price" name="price">
                </div>
                <div class="form-group">
                    <label for="app_description">App Description:</label>
                    <input type="text" id="app_description" name="app_description">
                </div>
                <div class="form-group">
                    <label for="dev_id">Developer ID:</label>
                    <input type="number" id="dev_id" name="dev_id" required>
                </div>
                <div class="form-group">
                    <label for="app_path">App Path:</label>
                    <input type="text" id="app_path" name="app_path" required>
                </div>
                <div class="form-group">
                    <label for="icon_path">Icon Path:</label>
                    <input type="text" id="icon_path" name="icon_path" required>
                </div>
            `;
        } else if (entity === 'category') {
            formContainer.innerHTML = `
                <div class="form-group">
                    <label for="cat_name">Category Name:</label>
                    <input type="text" id="cat_name" name="cat_name" required>
                </div>
                <div class="form-group">
                    <label for="cat_description">Category Description:</label>
                    <input type="text" id="cat_description" name="cat_description">
                </div>
            `;
        }
    }
}

function showUpdateForm(id, entity) {
    const updateFormContainer = document.getElementById(`update-form-container-${id}`);
    updateFormContainer.style.display = 'block';
}

function confirmDelete(id, entity) {
    if (confirm('Are you sure you want to delete this item?')) {
        window.location.href = `/delete/${entity}/${id}`;
    }
}