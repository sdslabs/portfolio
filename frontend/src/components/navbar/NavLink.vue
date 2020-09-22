<template>
    <a
        v-if="native"
        :href="url"
        :class="last ? 'mr-0' : 'mr-20'"
        class="no-underline block mt-8 sm:inline-block sm:mt-0"
        target="_blank"
    >
        <span class="block text-black py-3 text-xl sm:text-base">{{
            text
        }}</span>
    </a>
    <router-link
        v-else
        :to="url"
        :class="last ? 'mr-0' : 'mr-20'"
        class="no-underline block mt-8 sm:inline-block sm:mt-0"
    >
        <span class="block text-black text-xl sm:text-base py-3">{{
            text
        }}</span>
    </router-link>
</template>

<script>
export default {
    name: "NavLink",
    props: {
        native: Boolean,
        last: Boolean,
        url: String,
        text: String
    }
};
</script>

<style scoped>
.router-link-active {
    @apply font-semibold;
}

@screen sm {
    .router-link-active span {
        @apply border-black border-solid border-l-0 border-r-0 border-t-0 border-b-2;
    }
}
</style>
