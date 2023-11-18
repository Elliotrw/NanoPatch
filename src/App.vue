<script setup>
import ValueTabs from './components/ValueTabs.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/NanoPatch.png" />
    <!-- <div class="greetings">
      <h1 class="green">NanoPatch</h1>
    </div> -->
    <!-- <div class="wrapper">
    </div> -->
  </header>

  <main>
    <ValueTabs />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  max-width: 75%;
  max-height: 75%;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
