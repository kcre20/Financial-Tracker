<script setup>
import { ref, onMounted } from 'vue'

let balance = 100
let expenses = [
  { name: 'hawtpot', amount: 100, category: "food" },
  { name: 'christmas gifts', amount: 50, category: "frens" }
];

</script>

<template>
  <div id="balance">
    <div>
      Balance:
    </div>
    <div class="amount">
      ${{ balance }}
    </div>
  </div>

  <div class="monthly_overview">
    <div class="titles">
      <!-- want this to be selectable -->
      January
    </div>
    <div class="month_stats">
      <div class="month_income">
        Income: $1000
      </div>
      <div class="vertical_line"></div>
      <div class="month_expenses">
        Expenses: -$900
      </div>
    </div>
  </div>

  <div class="titles">
    Recent Expenses:
  </div>
  <table>
  <tr>
    <th>Expense Name</th>
    <th>Amount</th>
    <th>Category</th>
  </tr>
  <tr v-for="(expense, index) in expenses" :key="index">
    <td>{{ expense.name }}</td>
    <td>{{ expense.amount }}</td>
    <td>{{ expense.category }}</td>
  </tr>
</table>
</template>

<style>
#balance {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
}

.amount {
  font-size: 3rem;
  font-weight: bold;
}

.month_stats {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
}

.vertical_line {
  border-left: 1px solid black;
  height: 1rem;
  align-self: stretch;
}

.month_expenses,
.month_income {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  height: 5rem;
  border-radius: 5px;
  border-width: 0;
  border-style: solid;
}

.month_income {
  border-style: solid;
  border-color: green;
  color: green;
}

.month_expenses {
  border-style: solid;
  border-color: red;
  color: red;
}

.titles {
  font-size: 2rem;
  font-weight: bold;
  font-display: flex;
  text-align: center;
}

.recent_expenses {
  display: flex;
  align-items: center;
  flex-direction: column;

}

.expense {
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.expense_name {
  margin-right: 1rem;
}

.expense_amount {
  margin-left: 1rem;
}

th {
  text-align: left;
}

</style>
