<template>
    <div class="w-event h-auto shadow-feed pl-10 pt-10 pr-10">
        <Label :text="event.types" />
        <div class="flex flex-col mt-10 pb-10">
            <div class="font-extrabold text-xl leading-180">
                {{ event.title }}
            </div>
            <div class="mt-20 text-base leading-normal">
                {{ event.description }}
            </div>
        </div>
        <div class="mt-8 font-extrabold text-base text-blue mb-8 leading-170">
            Check Now
        </div>
    </div>
</template>

<script>
import Label from "@/components/Label.vue";
export default {
    name: "smallfeed",
    components: {
        Label
    },
    props: {
        event: Object
    }
}
</script>
