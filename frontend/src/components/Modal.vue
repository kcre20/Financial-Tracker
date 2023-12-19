<script setup>
</script>

<template>
    <div class="closeButton">
        <span class="close" @click="$emit('close')">&times;</span>
    </div>
    
<form>
    <label for="expense_name">Expense Name:</label><br>
    <input type="text" id="expense_name" name="expense_name"><br>
    <label for="expense_amount">Expense Amount:</label><br>
    <input type="number" id="expense_amount" name="expense_amount" step=".01"><br>
    <label for="expense_category">Expense Category:</label><br>
    <select id="expense_category" name="expense_category">
        <option value="food">Food</option>
        <option value="transportation">Transportation</option>
        <option value="utilities">Utilities</option>
        <option value="clothing">Clothing</option>
        <option value="medical">Medical</option>
        <option value="personal">Personal</option>
        <option value="education">Education</option>
        <option value="savings">Savings</option>
        <option value="gifts">Gifts</option>
        <option value="entertainment">Entertainment</option>
        <option value="other">Other</option>
    </select><br>
    <label for="expense_date">Expense Date:</label><br>
    <input type="text" id="expense_name" name="expense_name"><br>
    <!-- <input type="submit" value="Submit"> -->
    <div class="submitButton" @click="$emit('addExpense')">
        Submit
    </div>
</form>
</template>

<style>
.submitButton {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    cursor: pointer;
    margin-top: 2rem; 
}
.closeButton {
    display: flex;
    justify-content: flex-end;
    cursor: pointer;
    padding: 5px 32px;
}
.closeButton > span {
    font-size: 40px;
    font-weight: bold;
    color: #f44336;
}
</style>
<!-- use css to change the modal inputs -->
<!-- use js to add the expense to the database -->
<!-- try making ur own calendar -->
<!-- supabase for database -->