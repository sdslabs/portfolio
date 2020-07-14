<template>
    <div>
        <div
            class="mt-12 font-bold sm:font-extrabold text-1.5xl sm:text-base leading-180"
        >
            {{ title.toUpperCase() }}
        </div>
        <div
            v-if="url != null"
            class="mt-5 text-1.5xl sm:text-base text-grey leading-normal"
        >
            <a :href="url" target="_blank">{{
                timing ? timing : description
            }}</a>
        </div>
        <div
            v-else
            class="mt-5 text-1.5xl sm:text-base text-grey leading-normal"
        >
            {{ timing ? timing : description }}
        </div>
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
