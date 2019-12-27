<template>
    <div>
        <div class="mt-12 font-extrabold text-base leading-180">
            {{ title.toUpperCase() }}
        </div>
        <div v-if="url != null" class="mt-5 text-base leading-normal"><a :href="url" target="_blank">{{ timing ? timing : description }}</a></div>
        <div v-else class="mt-5 text-base leading-normal">{{ timing ? timing : description }}</div>
    </div>
</template>

<script>
export default {
    name: "updateCard",
    props: {
        title: String,
        url: String,
        timing: String,
        description: String
    }
};
</script>
