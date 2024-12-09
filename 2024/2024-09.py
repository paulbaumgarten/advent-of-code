import math, random, numpy, os, re, copy, time

DEMO = """2333133121414131402""".splitlines()

# 00...111...2...333.44.5555.6666.777.888899

# 00...111...2...333.44.5555.6666.777.888899

class Block:
    def __init__(self, length, id=None):
        self.length = length
        self.id = id

    def expand(self):
        if self.id is None:
            return "." * self.length
        else:
            return str(self.id) * self.length
    
    def is_free_space(self):
        return self.id==None
    
    def __repr__(self):
        return f"Block( length={self.length}, id={self.id} )"

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def print_sequence(blocks):
    for i in range(0, len(blocks)):
        print( blocks[i].expand(), end="")
    print()

def part1a(raw):
    data = DEMO[0]
    data = raw[0]
    id = 0
    file_space = True
    blocks = []
    # Read sequence into blocks
    for i,ch in enumerate(data):
        if file_space:
            blocks.append( Block(int(ch), id) )
            id += 1
        else: # free space 
            blocks.append( Block(int(ch), None) )
        file_space = not file_space
    # Iterate sequence
    print_sequence(blocks)
    # Compression
    forward_idx = 0
    backward_idx = len(blocks)-1
    while forward_idx < len(blocks)-1:
        #print_sequence(blocks)
        #print("forward_idx",forward_idx, "len(blocks)",len(blocks),"current block ",blocks[forward_idx])
        block_to_insert = blocks.pop()
        if block_to_insert.is_free_space():
            #print("just removed free space from end, next block")
            continue
        free_blocks_required = block_to_insert.length
        #print( "block to move forward ",block_to_insert,"\n")
        while free_blocks_required > 0:
            # if no free space, move on to the next
            if not blocks[forward_idx].is_free_space():
                forward_idx += 1
                continue
            # if correct amt of space, fill it
            if blocks[forward_idx].length == free_blocks_required:
                blocks[forward_idx].id = block_to_insert.id
                free_blocks_required = 0
                forward_idx += 1
            # if less than amt of space needed, fill it and keep track of how much more to fill
            elif blocks[forward_idx].length < free_blocks_required:
                blocks[forward_idx].id = block_to_insert.id
                free_blocks_required -= blocks[forward_idx].length
                forward_idx += 1
                if forward_idx >= len(blocks):
                    blocks.append(Block(free_blocks_required, block_to_insert.id))
                    free_blocks_required = 0
            # if more than amt of space, spit it, fill one, keep one empty
            elif blocks[forward_idx].length > free_blocks_required:
                original_length = blocks[forward_idx].length
                blocks[forward_idx] = block_to_insert
                blocks.insert(forward_idx+1, Block(original_length-block_to_insert.length, None))
                forward_idx += 1
                free_blocks_required = 0
    print_sequence(blocks)
    # Generate checksum
    pos = 0
    checksum = 0
    for i in range(0, len(blocks)):
        print(f"  ** BLOCK ** ",i,blocks[i],blocks[i].length,type(blocks[i].length))
        l = blocks[i].length
        for j in range(0, l):
            print(f"position {pos+j} block id {blocks[i].id}")
            checksum += (pos+j) * blocks[i].id
        pos += blocks[i].length
    print("checksum",checksum)
    return checksum
    # 9392001946363 too high
    # 6356833654075 correct
    # 0099811188827773336446555566
    # 0099811188827773336446555566


def part1(raw):
    data = DEMO[0]
    data = raw[0]
    id = 0
    file_space = True
    # Read sequence into blocks
    blocks = []
    for i,ch in enumerate(data):
        if file_space:
            for j in range(0, int(ch)):
                blocks.append( id )
            id += 1
        else: # free space 
            for j in range(0, int(ch)):
                blocks.append( None )
        file_space = not file_space
    #print(blocks)
    # Fill free space
    front = 0
    while front < len(blocks)-1:
        if blocks[front] is None:
            rear = blocks.pop()
            while rear is None:
                rear = blocks.pop()
            if front < len(blocks):
                blocks[front] = rear
            else:
                blocks.append(rear)
        front += 1
    #print(blocks)
    print("number of blocks: ",len(blocks))
    print(blocks[-10:])
    # Checksum
    checksum = 0
    for i in range(0, len(blocks)):
        checksum += i * blocks[i]
    print(checksum)
    return checksum
    # 6356833654075 correct

def locate_max_file(blocks, less_than=99999):
    pos = len(blocks)-1
    while (blocks[pos] == None) or (blocks[pos] >= less_than):
        #print(f"pos ",pos," less_than ",less_than, " blocks[pos] ",blocks[pos])
        pos -= 1
        if pos < 0:
            return 0, 0, 0
    fileid = blocks[pos]
    length = 0
    while blocks[pos] == fileid:
        pos -= 1
        length += 1
    pos += 1
    return pos, length, fileid

def locate_free_blocks(blocks, min_length=1):
    start_of_free_space = -1
    length_of_free_space = 0
    for i in range(0, len(blocks)):
        if blocks[i] == None:
            if start_of_free_space < 0:
                start_of_free_space = i
                length_of_free_space = 1
            else:
                length_of_free_space += 1
            if length_of_free_space >= min_length:
                return start_of_free_space
        else:
            start_of_free_space = -1
            length_of_free_space = 0
    return None

def swap_blocks(blocks, pos1, pos2, length):
    #print(blocks[pos1:pos1+length], blocks[pos2:pos2+length])
    for i in range(0, length):
        #print("swapping ",pos1+i,blocks[pos1+i],"with",pos2+i,blocks[pos2+i])
        tmp1 = blocks[pos1+i]
        tmp2 = blocks[pos2+i]
        blocks[pos1+i] = tmp2
        blocks[pos2+i] = tmp1
        #print(blocks[pos1:pos1+length], blocks[pos2:pos2+length])
    return blocks

def part2(raw):
    data = DEMO[0]
    data = raw[0]
    id = 0
    file_space = True
    # Read sequence into blocks
    blocks = []
    for i,ch in enumerate(data):
        if file_space:
            for j in range(0, int(ch)):
                blocks.append( id )
            id += 1
        else: # free space 
            for j in range(0, int(ch)):
                blocks.append( None )
        file_space = not file_space
    print(blocks,"\n")
    # Fill free space
    front = 0
    last_value_tried = 99999
    while True:
        #time.sleep(1)
        pos, length, id = locate_max_file(blocks, last_value_tried)
        if (pos==0 and length==0 and id==0):
            break
        print("Target blocks to move at ",pos,"length",length," id ",id)
        pos_free= locate_free_blocks(blocks, length)
        if pos_free != None and pos_free < pos:
            #print("free blocks found at ",pos_free)
            print("  -> swapping blocks with free at ",pos_free)
            blocks = swap_blocks(blocks, pos_free, pos, length)
        last_value_tried = id
        #print(blocks,"\n")
    
    #print(blocks)
    print("number of blocks: ",len(blocks))
    print("1st 25",blocks[:25])
    print("last 25",blocks[-25:])
    # Checksum
    checksum = 0
    for i in range(0, len(blocks)):
        if blocks[i] != None:
            checksum += i * blocks[i]
    print(checksum)
    return checksum
    # 6392923654416 too high
    # 6389911791746
    
if __name__=="__main__":
    start = time.time()
    #result = part1a(get_data())
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


