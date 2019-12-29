<template>
    <div class="gallery flex flex-col w-auto sm:w-gallery">
        <img
            class="sm:h-128 sm:w-180 rounded-lg"
            v-bind:src="slides[queue-1].image"
            alt="image"
        />
        <div
            class="textbox w-auto ml-6 mr-6 h-auto min-h-64 -mt-32 pr-6 sm:w-120 sm:h-auto sm:min-h-88 sm:ml-98 sm:-mt-gallery bg-white z-20"
        >
            <div class="font-extrabold text-2xl sm:text-lg mt-10 ml-10">{{slides[queue-1].title}}</div>
            <div
                class="sm:w-104 leading-170 text-grey text-xl sm:text-base mt-8 ml-10 mb-8"
            >
                {{slides[queue-1].description}}
            </div>
        </div>
        <div class="self-center sm:self-start sm:-mt-32">
            <span class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16" v-bind:class="{'bg-black': queue===1, 'bg-carousel': queue!==1}"/>
            <span class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4" v-bind:class="{'bg-black': queue===2, 'bg-carousel': queue!==2}"/>
            <span class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4" v-bind:class="{'bg-black': queue===3, 'bg-carousel': queue!==3}"/>
            <span class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4" v-bind:class="{'bg-black': queue===4, 'bg-carousel': queue!==4}"/>
        </div>
    </div>
</template>

<script>
import lectures from "@/assets/images/lectures.svg";
import hackathons from "@/assets/images/hackathons.svg";
import workshops from "@/assets/images/workshops.svg";
import competitions from "@/assets/images/competitions.svg";
export default {
    name: "Gallery",
    data: function initData() {
        return {
            slides: [
                {
                    image: lectures,
                    title: "Lectures",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    image: hackathons,
                    title: "SDSLabs Hackathon",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Lorem ipsum dolor"
                },
                {
                    image: workshops,
                    title: "Workshops",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. sagittis fringilla tempor."
                },
                {
                    image: competitions,
                    title: "Competitions",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam feugiat porta vitae sit amet ligula."
                }
            ],
            queue: 1
        };
    },
    methods: {
        carousel: function() {
            setInterval(() => {
                if (this.queue % 4 !== 0) {
                    this.queue++;
                } else this.queue = 1;
            }, 2000);
        }
    },
    mounted() {
        this.carousel();
    }
};
</script>

<style scoped lang="scss">
.textbox {
    box-shadow: 0px 6px 30px rgba(0, 0, 0, 0.07);
    border-radius: 5px;
}
</style>
