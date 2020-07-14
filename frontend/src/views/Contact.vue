<template>
    <div class="flex flex-col sm:pt-60 pt-48 w-full overflow-x-hidden">
        <div
            class="flex flex-col sm:flex-row mb-60 items-center justify-between sm:justify-between flex-col pl-0 pr-0"
        >
            <div
                class="flex flex-col ml-8 mr-8 sm:w-auto sm:pl-60 pr-0 sm:pt-20 sm:pt-0"
            >
                <div class="text-3xl font-extrabold">SAY HELLO!</div>
                <div
                    class="sm:w-168 pt-12 sm:pt-6 text-1.5xl sm:text-base sm:font-medium text-grey leading-170"
                >
                    Gotta discuss something with us or just wanna say hello,
                    we’re always up for a chat.
                </div>
                <div class="sm:-mt-4">
                    <Button
                        class="mt-14 bg-purple"
                        v-bind:native="true"
                        url="https://chat.sdslabs.co/"
                        text="chat.sdslabs.co"
                        :image="
                            require('@/assets/images/button-arrow-small.svg')
                        "
                    />
                </div>
                <div
                    class="sm:w-168 mt-24 text-1.5xl sm:text-base sm:font-medium text-grey leading-170"
                >
                    Or find us on these platforms:
                </div>
                <div class="flex flex-row justify-center mt-12 mr-14">
                    <div class="mr-14">
                        <a
                            href="https://github.com/sdslabs"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-14"
                                alt="github"
                                src="@/assets/images/github.svg"
                            />
                        </a>
                    </div>
                    <div class="mr-14">
                        <a
                            href="https://feedburner.google.com/fb/a/mailverify?uri=sdslabs/IOpf1&loc=en_US"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-12 mt-2"
                                alt="gmail"
                                src="@/assets/images/gmail.svg"
                            />
                        </a>
                    </div>
                    <div class="mr-14">
                        <a
                            href="https://medium.com/sdslabs"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-12 mt-2"
                                alt="medium"
                                src="@/assets/images/medium.svg"
                            />
                        </a>
                    </div>
                    <div class="mr-14">
                        <a
                            href="https://www.facebook.com/SDSLabs"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-14"
                                alt="facebook"
                                src="@/assets/images/facebook.svg"
                            />
                        </a>
                    </div>
                    <div class="mr-14">
                        <a
                            href="https://twitter.com/sdslabs"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-16"
                                alt="twitter"
                                src="@/assets/images/twitter.svg"
                            />
                        </a>
                    </div>
                    <div>
                        <a
                            href="https://www.instagram.com/sdslabs/"
                            rel="noopener noreferrer"
                            target="blank"
                        >
                            <img
                                class="h-16"
                                alt="instagram"
                                src="@/assets/images/instagram.svg"
                            />
                        </a>
                    </div>
                </div>
            </div>

            <div
                class="flex flex-row justify-center mt-32 sm:mt-12 ml-8 mr-8 sm:ml-64 sm:mr-60 mb-44 sm:mb-0"
            >
                <img
                    class="relative"
                    src="../assets/images/think-build-ship-pic.png"
                />
                <div
                    class="textbox absolute mt-120 sm:mt-64 sm:-ml-81 mt-76 bg-white  shadow-sister p-10 sm:pr-0 h-80 z-20"
                >
                    <div class="w-140 sm:w-120 flex flex-row">
                        <img
                            class="mr-8 mt-1"
                            sm:src="../assets/images/location.svg"
                            src="../assets/images/location-small.svg"
                        />
                        <div class="font-bold text-xl sm:text-lg leading-170">
                            Our doors are always open, come visit us at :
                        </div>
                    </div>
                    <div
                        class="w-144 sm:w-120 leading-170 text-grey text-xl sm:text-base mt-8"
                    >
                        SDSLabs, New SAC Building, Thomson Marg IIT Roorkee,
                        Roorkee, Uttarakhand 247667
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Button from "@/components/Button.vue";
export default {
    name: "Error404",
    components: {
        Button
    }
};
</script>
