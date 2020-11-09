class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_map = collections.defaultdict(list)
        for proc_index in range(len(ppid)):
            child_map[ppid[proc_index]].append(pid[proc_index])
        kill_queue = []
        kill_queue.append(kill)
        killed_ids = []
        while kill_queue:
            for _ in range(len(kill_queue)):
                proc_id = kill_queue.pop()
                killed_ids.append(proc_id)
                if proc_id in child_map:
                    kill_queue.extend(child_map[proc_id])
        return killed_ids
