<template>
    <div class="home-wrapper">
        <Landing />
    </div>
</template>

<script>

import Landing from "@/components/Landing.vue";

export default {
    name: "home",
    components: {
        Landing
    }
};
</script>

<style scoped lang="scss">
.banner {
    padding-top: 7.4rem;
    height: 80vh;
}

.banner-footer {
    height: 20vh;
}

.text-justify {
    text-align-last: center;
}
</style>
