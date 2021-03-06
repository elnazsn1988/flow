"""Flow - Algorithmic HF trader

   Copyright 2016, Yazan Obeidi

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from qlearn import QLearn

__author__ = 'yazan'

class Learning(QLearn):
    """
    This class links all learning modules a trader might use together.
    """
    def __init__(self, q, alpha, reward, discount, initial_state, actions):
        self.q = {}
        self.alpha = alpha
        self.reward = reward
        self.discount = discount
        self.states = initial_state
        QLearn.__init__(self, actions, len(initial_state), alpha)
