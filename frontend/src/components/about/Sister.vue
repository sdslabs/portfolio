<template>
    <div class="flex flex-col w-144 h-96 shadow-sister">
        <div class="flex flex-row mt-8">
            <div><img class="ml-12 w-56 h-40" :src="url" /></div>
            <div class="mt-12 mx-12 leading-160 font-semibold text-lg w-96">
                {{ title }}
            </div>
        </div>
        <div
            class="mt-6 ml-10 mr-12 text-1.5xl sm:text-base text-grey leading-normal"
        >
            {{ description }}
        </div>
    </div>
</template>

<script>
export default {
    name: "sister",
    props: {
        url: String,
        title: String,
        description: String
    }
};
</script>
