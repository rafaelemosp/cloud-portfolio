const nameElement = document.getElementById("typing-name");

const fullName = "Rafael Lemos";

let index = 0;

function typeName() {
    if (!nameElement) {
        return;
    }

    if (index < fullName.length) {
        nameElement.innerHTML =
            fullName.substring(0, index + 1) +
            '<span class="cursor">|</span>';

        index++;

        setTimeout(typeName, 120);
    } else {
        nameElement.innerHTML =
            fullName +
            '<span class="cursor">|</span>';
    }
}

const reducedMotionQuery = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
);

if (nameElement) {
    if (reducedMotionQuery.matches) {
        nameElement.textContent = fullName;
    } else {
        typeName();
    }
}

const networkCanvas = document.getElementById("network-background");

if (networkCanvas) {
    const ctx = networkCanvas.getContext("2d");

    let width = window.innerWidth;
    let height = window.innerHeight;
    let animationFrameId;
    let startTime = performance.now();

    const mapWidth = 1000;
    const mapHeight = 500;

    const continents = [
        [[65, 105], [115, 65], [190, 70], [245, 115], [225, 175],
            [180, 200], [155, 250], [120, 225], [95, 170]],
        [[240, 235], [285, 260], [305, 325], [285, 400], [250, 455],
            [220, 390], [215, 310]],
        [[425, 105], [475, 80], [535, 105], [520, 145], [470, 160],
            [435, 140]],
        [[455, 175], [525, 170], [565, 225], [545, 330], [495, 385],
            [455, 310], [430, 235]],
        [[525, 105], [630, 65], [760, 90], [880, 135], [895, 210],
            [820, 235], [755, 195], [700, 225], [625, 180], [560, 170]],
        [[805, 325], [865, 300], [925, 330], [910, 385], [845, 400],
            [800, 365]]
    ];

    const hubs = [
        { name: "Virginia", x: 205, y: 170, size: 5 },
        { name: "California", x: 125, y: 185, size: 4 },
        { name: "Sao Paulo", x: 265, y: 345, size: 4 },
        { name: "Ireland", x: 465, y: 125, size: 5 },
        { name: "Frankfurt", x: 505, y: 135, size: 4 },
        { name: "Cape Town", x: 500, y: 350, size: 4 },
        { name: "Mumbai", x: 685, y: 215, size: 4 },
        { name: "Singapore", x: 770, y: 265, size: 5 },
        { name: "Tokyo", x: 860, y: 165, size: 4 },
        { name: "Sydney", x: 865, y: 355, size: 6 }
    ];

    const routes = [
        [0, 1], [0, 2], [0, 3], [1, 9], [2, 5], [2, 9],
        [3, 4], [3, 7], [4, 5], [4, 6], [4, 8], [5, 9],
        [6, 7], [6, 8], [7, 8], [7, 9], [8, 9]
    ];

    function getMapLayout() {
        const availableWidth = width * 0.96;
        const availableHeight = height * 0.82;
        const scale = Math.min(
            availableWidth / mapWidth,
            availableHeight / mapHeight
        );

        return {
            scale,
            offsetX: (width - mapWidth * scale) / 2,
            offsetY: (height - mapHeight * scale) / 2
        };
    }

    function mapPoint(point, layout) {
        return {
            x: layout.offsetX + point.x * layout.scale,
            y: layout.offsetY + point.y * layout.scale
        };
    }

    function resizeCanvas() {
        const pixelRatio = window.devicePixelRatio || 1;

        width = window.innerWidth;
        height = window.innerHeight;

        networkCanvas.width = width * pixelRatio;
        networkCanvas.height = height * pixelRatio;
        networkCanvas.style.width = `${width}px`;
        networkCanvas.style.height = `${height}px`;

        ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
    }

    function drawWorldMap(layout) {
        ctx.save();
        ctx.translate(layout.offsetX, layout.offsetY);
        ctx.scale(layout.scale, layout.scale);
        ctx.fillStyle = "rgba(88, 166, 255, 0.11)";
        ctx.strokeStyle = "rgba(88, 166, 255, 0.28)";
        ctx.lineWidth = 1.4 / layout.scale;
        ctx.shadowColor = "rgba(31, 111, 235, 0.22)";
        ctx.shadowBlur = 18 / layout.scale;

        continents.forEach((continent) => {
            ctx.beginPath();
            ctx.moveTo(continent[0][0], continent[0][1]);

            for (let i = 1; i < continent.length; i += 1) {
                ctx.lineTo(continent[i][0], continent[i][1]);
            }

            ctx.closePath();
            ctx.fill();
            ctx.stroke();
        });

        ctx.shadowBlur = 0;
        ctx.restore();
    }

    function getRouteGeometry(route, layout) {
        const start = mapPoint(hubs[route[0]], layout);
        const end = mapPoint(hubs[route[1]], layout);
        const distance = Math.hypot(end.x - start.x, end.y - start.y);

        return {
            start,
            end,
            control: {
                x: (start.x + end.x) / 2,
                y: (start.y + end.y) / 2 - Math.min(70, distance * 0.18)
            }
        };
    }

    function drawRoutes(layout) {
        routes.forEach((route) => {
            const geometry = getRouteGeometry(route, layout);

            ctx.beginPath();
            ctx.moveTo(geometry.start.x, geometry.start.y);
            ctx.quadraticCurveTo(
                geometry.control.x,
                geometry.control.y,
                geometry.end.x,
                geometry.end.y
            );
            ctx.strokeStyle = "rgba(88, 166, 255, 0.3)";
            ctx.lineWidth = 1.15;
            ctx.stroke();
        });
    }

    function drawHubs(layout, elapsed) {
        hubs.forEach((hub, hubIndex) => {
            const point = mapPoint(hub, layout);
            const pulse = 1 + Math.sin(elapsed * 0.0018 + hubIndex) * 0.18;
            const radius = hub.size * pulse;

            ctx.beginPath();
            ctx.arc(point.x, point.y, radius * 2.5, 0, Math.PI * 2);
            ctx.fillStyle = "rgba(88, 166, 255, 0.055)";
            ctx.fill();

            ctx.beginPath();
            ctx.arc(point.x, point.y, radius, 0, Math.PI * 2);
            ctx.fillStyle = "rgba(88, 166, 255, 0.9)";
            ctx.shadowColor = "rgba(88, 166, 255, 0.8)";
            ctx.shadowBlur = 14;
            ctx.fill();

            ctx.beginPath();
            ctx.arc(point.x, point.y, Math.max(1.5, radius * 0.35), 0, Math.PI * 2);
            ctx.fillStyle = "rgba(230, 246, 255, 0.95)";
            ctx.fill();
            ctx.shadowBlur = 0;
        });
    }

    function quadraticPoint(geometry, progress) {
        const inverse = 1 - progress;

        return {
            x: inverse * inverse * geometry.start.x +
                2 * inverse * progress * geometry.control.x +
                progress * progress * geometry.end.x,
            y: inverse * inverse * geometry.start.y +
                2 * inverse * progress * geometry.control.y +
                progress * progress * geometry.end.y
        };
    }

    function drawPackets(layout, elapsed) {
        routes.forEach((route, routeIndex) => {
            const geometry = getRouteGeometry(route, layout);
            const progress = (elapsed * 0.00009 + routeIndex * 0.137) % 1;
            const point = quadraticPoint(geometry, progress);

            ctx.beginPath();
            ctx.arc(point.x, point.y, 2.2, 0, Math.PI * 2);
            ctx.fillStyle = "rgba(126, 231, 135, 0.95)";
            ctx.shadowColor = "rgba(126, 231, 135, 0.95)";
            ctx.shadowBlur = 12;
            ctx.fill();
            ctx.shadowBlur = 0;
        });
    }

    function drawNetwork(elapsed, includePackets = true) {
        const layout = getMapLayout();

        ctx.clearRect(0, 0, width, height);
        drawWorldMap(layout);
        drawRoutes(layout);
        drawHubs(layout, elapsed);

        if (includePackets) {
            drawPackets(layout, elapsed);
        }
    }

    function animateNetwork(timestamp) {
        drawNetwork(timestamp - startTime);

        animationFrameId = window.requestAnimationFrame(
            animateNetwork
        );
    }

    function drawStaticNetwork() {
        drawNetwork(0, false);
    }

    function initialiseNetwork() {
        resizeCanvas();

        window.cancelAnimationFrame(animationFrameId);

        if (reducedMotionQuery.matches) {
            drawStaticNetwork();
        } else {
            startTime = performance.now();
            animateNetwork(performance.now());
        }
    }

    initialiseNetwork();

    window.addEventListener("resize", initialiseNetwork);

    function handleMotionPreferenceChange() {
        window.cancelAnimationFrame(animationFrameId);

        if (reducedMotionQuery.matches) {
            if (nameElement) {
                nameElement.textContent = fullName;
            }
            drawStaticNetwork();
        } else {
            startTime = performance.now();
            animateNetwork(performance.now());
        }
    }

    reducedMotionQuery.addEventListener(
        "change",
        handleMotionPreferenceChange
    );
}
