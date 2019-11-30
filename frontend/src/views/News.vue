<template>
    <div class="flex flex-col pt-56 pl-56 w-full">
        <div class="flex flex-col">
            <div class="font-black text-3xl">News Updates</div>
            <div class="w-largetext text-base mt-10 leading-normal">Lorem ipsum dolor sit amet, adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, adipiscing elit.</div>
        </div>
        <div class="flex flex-row pt-28 pr-navbar">
            <div class="flex flex-col">
                <div class="w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar">
                    <Label text="UPCOMING EVENT"/>
                    <div class="flex flex-col h-72 mt-12 border-b-feed border-border pb-12">
                        <div class="font-extrabold text-xl">SYNTAX ERROR - CAMPUS HACKATHON</div>
                        <div class="mt-8 text-base font-semibold">27 - 30th September, 2018</div>
                        <div class="mt-16 text-base">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</div>
                    </div>
                    <div class="flex flex-col mt-12 pb-10">
                        <div class="font-semibold text-base">2 Updates</div>
                        <div class="mt-12 font-extrabold text-base">Answering Your Questions</div>
                        <div class="mt-5 text-base">As many of you have similar questions regarding teams and topics, we decided to come up with this post.</div>
                        <div class="mt-12 font-extrabold text-base">Opening Talk</div>
                        <div class="mt-5 text-base">28th September, 2018 | 7:00 PM | LHC 005</div>
                    </div>
                    <div class="mt-10 font-extrabold text-base text-red mb-8">Know more</div>
                </div>
                <div class="mt-10 w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar mb-64">
                    <Label text="PAST EVENT"/>
                    <div class="flex flex-col pb-14">
                        <div class="mt-14 font-extrabold text-xl">LINUX PARTY</div>
                        <div class="mt-8 font-semibold text-base">19th August, 2018</div>
                        <div class="mt-14 text-base">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. </div>
                    </div>
                    <div class="mt-10 font-extrabold text-base text-green mb-8">Know more</div>
                </div>
            </div>
            <div class="flex flex-col ml-10">
                <div class="flex flex-row">
                    <div class="w-event h-auto shadow-feed pl-10 pt-10 pr-10">
                        <Label text="APP UPDATE"/>
                        <div class="flex flex-col mt-10 pb-10">
                            <div class="font-extrabold text-xl leading-180">MUZI</div>
                            <div class="mt-20 text-base">The album Haider by Vishal Bharadwaj is now available on Muzi.</div>
                        </div>
                        <div class="mt-8 font-extrabold text-base text-blue mb-8">Check Now</div>
                    </div>
                    <div class="w-event h-auto shadow-feed pl-10 pt-10 pr-10 ml-10">
                        <Label text="ONLINE COMPETITION"/>
                        <div class="flex flex-col mt-10 pb-10">
                            <div class="font-extrabold text-xl leading-180">CODEBLITZ</div>
                            <div class="mt-6 font-semibold text-base">25th September, 2018</div>
                            <div class="mt-14 text-base">Competetion starts at 9:00 PM on CodeVillage.</div>
                        </div>
                        <div class="mt-8 font-extrabold text-base text-yellow mb-8">Check Now</div>
                    </div>
                </div>
                <div class="mt-10 w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar mb-64">
                    <Label text="PAST EVENT"/>
                    <div class="flex flex-col pb-14">
                        <div class="mt-14 font-extrabold text-xl">WORKSHOP ON WEB DEVELOPMENT</div>
                        <div class="mt-8 font-semibold text-base">8th September, 2018</div>
                        <div class="mt-14 text-base">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</div>
                    </div>
                    <div class="flex flex-col pb-12 mt-14">
                        <div class="font-semibold text-base">1 Update</div>
                        <div class="mt-8 font-extrabold text-base">POST WORKSHOP PHOTOS</div>
                    </div>
                    <div class="mt-10 font-extrabold text-base text-purple mb-8">Know more</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Label from "@/components/Label.vue"
export default {
    name: "news",
    components: {
        Label
    }
};
</script>
