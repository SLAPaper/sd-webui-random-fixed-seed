# Copyright 2025 SLAPaper
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import typing as tg

import gradio as gr

import modules.scripts
import modules.ui_components

SEED_IDS: list[str] = [
    "txt2img_seed",
    "img2img_seed",
]


class RandomFixedSeed(modules.scripts.Script):
    """Random Fixed Seed Script"""

    def __init__(self) -> None:
        super().__init__()

        self.script_name = "Random Fixed Seed"
        self.script_description = "Generate new random fixed seeds."
        self.script_icon = "🔮"
        self.on_after_component_elem_id: list[tuple[str, tg.Callable]] = []

        for seed_id in SEED_IDS:
            self.on_after_component_elem_id.append((seed_id, self.add_seed_button))

    def title(self) -> str:
        """Return the title of the script."""
        return f"{self.script_icon} {self.script_name}"

    def show(self, is_img2img) -> bool | object:
        """Determine if the script should be shown based on the mode."""
        return modules.scripts.AlwaysVisible

    def add_seed_button(self, on_component: modules.scripts.OnComponent) -> None:
        button = modules.ui_components.ToolButton(
            self.script_icon,
            elem_id=f"{on_component.component.elem_id}-random-fixed-seed",
            tooltip=self.script_description,
        )
        button.click(
            fn=self.generate_random_fixed_seed,
            inputs=[on_component.component],
            outputs=[on_component.component],
        )

    def generate_random_fixed_seed(self, component: gr.Blocks) -> dict:
        """Generate a new random fixed seed."""
        seed = random.randint(0, 2**31 - 1)  # Generate a random seed
        return gr.update(value=seed)
