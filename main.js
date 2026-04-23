import * as THREE from 'three';
import gsap from 'gsap';
import Lenis from 'lenis';

/**
 * The Hoss Group Framework - 3D Starter
 */

// Smooth Scrolling (Lenis)
const lenis = new Lenis();
function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Three.js Setup
const canvas = document.querySelector('#canvas3d');
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
  antialias: true,
  alpha: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// Object
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x555555 }); // Neutral brand color for cube
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// Animation
gsap.to(cube.rotation, {
    x: Math.PI * 2,
    y: Math.PI * 2,
    duration: 5,
    repeat: -1,
    ease: "none"
});

// Resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
});

// Loop
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();

console.log('The Hoss Group 3D Infrastructure initialized.');
