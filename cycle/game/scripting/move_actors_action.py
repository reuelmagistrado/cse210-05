from game.scripting.action import Action


class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast, script):
        """Executes something that is important in the game.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
        return super().execute(cast, script)
