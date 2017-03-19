from toodledoclient.datatypes import Task

from utils import unlines


class HtmlTextFormater:
    def __init__(self):
        pass

    def task_list_fmt(self, tasks: [Task]):
        return "{}".format(unlines(map(
            lambda p: self.task_fmt(p[1], p[0]),
            enumerate(tasks, 1))))

    @staticmethod
    def tag_map(tag):
        tmap = {'edu': '\U0001F4D2'}
        tmap = {}
        return tmap.get(tag, '#' + tag)

    def task_fmt(self, task: Task, num=None):
        x = '\U00002714' if task.completed else '\U000025FD'
        x = '\U00002B50' if task.star else x
        due = '' if task.duedate is None else task.duedate.strftime("<i>%d %b, %A</i>")
        tags = str.join(' ', map(self.tag_map, task.tags))
        num = num or ''
        res = str.format("{x} {num} {title} {tags} {due}", x=x, title=task.title, due=due, tags=tags, num=num)
        return res