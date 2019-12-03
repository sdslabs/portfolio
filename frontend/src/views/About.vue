<template>
    <div class="flex flex-col pt-44 w-screen">
        <div class="area_of_interest">
            <div
                class="flex md:flex-row-reverse items-center md:justify-between flex-col"
            >
                <div class="mr-28 w-220">
                    <div class="flex rounded shadow-md absolute flex-row w-92 h-32">
                        <div class="m-8 w-20 h-20">
                            <img src="@/assets/images/interest1.png">
                        </div>
                        <div class="font-sans font-semibold self-center text-base align-middle leading-160">
                            Software Development
                        </div>
                    </div>
                    <div class="md:pt-0 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest2.png">
                            </div>
                            <div class="font-sans pr-10 font-semibold self-center text-base align-middle leading-160">
                                Information Security
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest3.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-base align-middle leading-160">
                                Product Design
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-20 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest4.png">
                            </div>
                            <div class="self-center font-sans font-semibold text-base leading-160">
                                Data Science
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest5.png">
                            </div>
                            <div class="font-sans font-semibold pr-8 text-base self-center leading-160">
                                Game Development
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:pl-56 relative w-180 h-76">
                    <div class="text-3xl font-black absolute mt-12">Area of Interest</div>
                    <div class="text-base w-180 mt-40 absolute font-semibold text-grey leading-170">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                        nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                        sit amet augue sit amet quam feugiat porta vitae sit amet
                        ligula. Nulla posuere pellentesque metus sit amet.
                    </div>
                </div>
            </div>
        </div>

        <div class="timeline">
            <div
                class="flex md:flex-col items-center md:justify-between flex-col mt-176 relative"
            >
                <div class="text-3xl font-black absolute">Timeline</div>
                <div class="text-base w-292 mt-28 text-center absolute font-semibold text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac 
                    lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque 
                    sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam 
                    feugiat porta vitae sit amet ligula.
                </div>
            </div>

            <div class="timeline_bar flex mt-88 align-bottom h-100 w-screen relative overflow-x-auto">
                <div class="flex flex-row-reverse flex-no-wrap" v-for="timeline in timelines" v-bind:key="timeline.id">
                    <div class="timeline-box shadow-md ml-5 mr-5 self-center w-144 p-10">
                        <div class="text-base font-semibold">{{ timeline.date }}</div>
                        <div class="text-lg text-grey-900 font-semibold pt-13">{{ timeline.title }}</div>
                        <div class="text-base text-grey pt-10 leading-normal">{{ timeline.description }}</div>
                    </div>
                </div>
            </div>

            <div class="scroll_icon">
                <button class="scroll_button" onclick="scrollFunction(timeline_bar)"><img class=" self-center w-16 h-16 w-screen mt-24" src="@/assets/images/scroll-arrow.svg"></button>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            timelines: [
                {
                    id: 6,
                    date: "March, 2018",
                    title: "Microsoft Code.Fun.do 2018",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 5,
                    date: "March, 2018",
                    title: "Microsoft Code.Fun.do 2018",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 4,
                    date: "February, 2018",
                    title: "LIVE Revamped",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing aenean lacinia"
                },
                {
                    id: 3,
                    date: "February, 2018",
                    title: "CTFtime ranking",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 2,
                    date: "January, 2018",
                    title: "Inter IIT Tech Meet",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximu"
                },
                {
                    id: 1,
                    date: "December, 2018",
                    title: "XYZ",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximu"
                },
            ]
        }
    },
    methods: {
        scrollFunction: function(className) {
            document.getElementsByClassName(className).scrollBy += 100;
            document.getElementsByClassName(className).scrollBy += 100;
        } 
    }
}

</script>

<style lang="scss" scoped>
.timeline_bar::-webkit-scrollbar {
    display: none;
}
.timeline_bar::-moz-osx-scrollbar {
    display: none;
}
</style>