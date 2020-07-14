<template>
    <div class="footer sticky h-96 z-20 bg-footer flex flex-col justify-center">
        <div class="font-extrabold leading-170 text-lg text-center">
            Made with <i class="fas fa-heart text-red"></i> by SDSLabs
        </div>
        <div class="flex flex-row justify-center mt-20">
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
</template>

<script>
export default {
    name: "Footer"
};
</script>
