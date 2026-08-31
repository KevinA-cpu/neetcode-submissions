class Solution:
    specialuuid = "cd67ffcc-88d9-4240-a0cd-406ad40900c8"
    emptymarker = "07d2b4ee-31d3-4ae7-846c-fd13878fdd3b"

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return self.emptymarker
        return self.specialuuid.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.emptymarker:
            return []
        return s.split(self.specialuuid)