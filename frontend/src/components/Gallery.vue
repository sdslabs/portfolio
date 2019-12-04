<template>
    <div class="gallery w-gallery">
        <img
            class="h-88 md:h-128 md:w-180"
            :src="slides[queue-1].image"
            alt="image"
        />
        <div
            class="textbox absolute w-96 h-64 ml-44 -mt-32 md:w-98 md:h-88 md:ml-98 md:mt-gallery bg-white z-30"
        >
            <div class="font-extrabold md:text-lg mt-10 ml-10">{{slides[queue-1].title}}</div>
            <div
                class="w-88 md:w-96 leading-170 text-grey md:text-base mt-8 ml-10"
            >
                {{slides[queue-1].description}}
            </div>
        </div>
        <div>
            <span class="h-3 w-3 rounded-50 inline-block bg-black mt-16"/>
            <span class="h-3 w-3 rounded-50 inline-block bg-black mt-16 ml-4"/>
            <span class="h-3 w-3 rounded-50 inline-block bg-black mt-16 ml-4"/>
            <span class="h-3 w-3 rounded-50 inline-block bg-black mt-16 ml-4"/>
        </div>
    </div>
</template>

<script>
export default {
    name: "Gallery",
    data: function initData() {
        return {
            slides: [
                {
                    image: "@/assets/images/lectures.svg",
                    title: "Lectures",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    image: "",
                    title: "SDSLabs Hackathon",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Lorem ipsum dolor"
                },
                {
                    image: "",
                    title: "Workshops",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. sagittis fringilla tempor."
                },
                {
                    image: "",
                    title: "Competitions",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam feugiat porta vitae sit amet ligula."
                }
            ],
            queue: 1
        }
    }
};
</script>

<style scoped lang="scss">
.textbox {
    box-shadow: 0px 6px 30px rgba(0, 0, 0, 0.07);
    border-radius: 5px;
}

</style>
