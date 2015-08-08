""" Connected components and graph resilience"""
__author__ = 'Amras'

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """Takes as input a set of characters alphabet and three scores diag_score, off_diag_score"""
    score_matrix_out={}
    ele_count_one=0;

    for ele_one in alphabet:
        score_matrix_in={}
        ele_count_two=0;
        for ele_two in alphabet:
            if ele_count_one == ele_count_two:
                score_matrix_in[ele_two]=diag_score;
            else:
                score_matrix_in[ele_two]=off_diag_score;
            ele_count_two+=1
        score_matrix_in['-']=dash_score
        score_matrix_out[ele_one]=score_matrix_in
        ele_count_one+=1

    score_matrix_in={}
    for ele in alphabet:
        score_matrix_in[ele]=dash_score;
    score_matrix_in['-']=dash_score;
    score_matrix_out['-']=score_matrix_in
    return score_matrix_out

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
        """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix"""
        alignment_matrix = [ [0 for col in range(len(seq_y)+1)] for row in range(len(seq_x)+1)]

        for col in range(len(seq_y)):
            result=alignment_matrix[0][col]+scoring_matrix['-'][seq_y[col]];
            if not global_flag:
                if result <= 0:
                    result=0
            alignment_matrix[0][col+1]=result
        for row in range(len(seq_x)):
            result=alignment_matrix[row][0]+scoring_matrix[seq_x[row]]['-'];
            if not global_flag:
                if result <=0:
                    result=0
            alignment_matrix[row+1][0]=result;

        for row in range(1,len(seq_x)+1):
            for col in range(1,len(seq_y)+1):
                one=alignment_matrix[row-1][col-1]+scoring_matrix[seq_x[row-1]][seq_y[col-1]]
                two=alignment_matrix[row-1][col]+scoring_matrix[seq_x[row-1]]['-']
                three=alignment_matrix[row][col-1]+scoring_matrix['-'][seq_y[col-1]]
                max_val=max(one,two,three)
                if not global_flag:
                    if max_val<=0:
                        max_val=0
                alignment_matrix[row][col]=max_val
        return alignment_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix"""
    row_index=len(seq_x)
    col_index=len(seq_y)
    align_x=[]
    align_y=[]
    score=0
    while row_index!=0 and col_index != 0:
        if alignment_matrix[row_index][col_index] == alignment_matrix[row_index-1][col_index-1]+scoring_matrix[seq_x[row_index-1]][seq_y[col_index-1]]:
            align_x.append(seq_x[row_index-1])
            align_y.append(seq_y[col_index-1])
            row_index-=1
            col_index-=1
        elif alignment_matrix[row_index][col_index] == alignment_matrix[row_index-1][col_index]+scoring_matrix[seq_x[row_index-1]]['-']:
            align_x.append(seq_x[row_index-1])
            align_y.append('-')
            row_index-=1
        else:
            align_x.append('-')
            align_y.append(seq_y[col_index-1])
            col_index-=1
    while row_index!= 0:
        align_x.append(seq_x[row_index-1])
        align_y.append('-')
        row_index-=1
    while col_index != 0:
        align_y.append(seq_y[col_index-1])
        align_x.append('-')
        col_index-=1

    score=alignment_matrix[len(seq_x)][len(seq_y)]
    align_x=''.join(align_x)
    align_y=''.join(align_y)
    align_x=align_x[::-1]
    align_y=align_y[::-1]
    return (score,align_x,align_y)

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix"""
    row_index=0
    col_index=0
    align_x=[]
    align_y=[]
    score=0
    row_iter=0;

    for row in alignment_matrix:
        col_iter=0
        for col in row:
            if col>=score:
                score=col;
                row_index=row_iter
                col_index=col_iter
            col_iter+=1
        row_iter+=1


    while row_index!=0 and col_index != 0:
        if alignment_matrix[row_index][col_index]!= 0:
            if alignment_matrix[row_index][col_index] == alignment_matrix[row_index-1][col_index-1]+scoring_matrix[seq_x[row_index-1]][seq_y[col_index-1]]:
                align_x.append(seq_x[row_index-1])
                align_y.append(seq_y[col_index-1])
                row_index-=1
                col_index-=1
            elif alignment_matrix[row_index][col_index] == alignment_matrix[row_index-1][col_index]+scoring_matrix[seq_x[row_index-1]]['-']:
                align_x.append(seq_x[row_index-1])
                align_y.append('-')
                row_index-=1
            else:
                align_x.append('-')
                align_y.append(seq_y[col_index-1])
                col_index-=1
        else :
            break
    align_x=''.join(align_x)
    align_y=''.join(align_y)
    align_x=align_x[::-1]
    align_y=align_y[::-1]
    return (score,align_x,align_y)
