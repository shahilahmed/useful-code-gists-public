void set_position(char *fen) {
	int r = 7, c = 0, sq = 0;
	//             "abcdefghijklmnopqrstuvwxyz"
	char sym[26] = ".2........5..1.043........";
	
	for(sq = 0; sq < 128; sq++) color[sq] = piece[sq] = 6;	
	
	king[0] = king[1] = side = castle = ep = fifty = -1;
	memset(counter,0,sizeof(counter));
	ply = hply = counter[0] = 0;
	
	while(!isspace(*fen)) {
		sq = ((r * 8) + c);
		if(*fen >= 'A' && *fen <= 'Z') {
			color[sq] = 0; piece[sq] = (sym[*fen - 'A'] - '0');
			if(*fen == 'K') king[0] = sq;
			c = c + 1;
		} else if(*fen >= 'a' && *fen <= 'z') {
			color[sq] = 1; piece[sq] = (sym[*fen - 'a'] - '0');
			if(*fen == 'k') king[1] = sq;
			c = c + 1;
		} else if(*fen >= '1' && *fen <= '8') {
			c = c + (*fen - '0');
		} else if(*fen == '/') {
			r = r - 1; c = 0;
		}
		fen++;
	}
	do { fen++; } while(isspace(*fen));
	switch(tolower(*fen)) {
		case 'w': side = 0; break;
		case 'b': side = 1; break;
	}
	do { fen++; } while(isspace(*fen));
	castle = 0;
	while(*fen != '\0' && !isspace(*fen)) {
		switch(*fen) {
			case 'K': castle |= 1; break; case 'Q': castle |= 2; break;
			case 'k': castle |= 4; break; case 'q': castle |= 8; break;
		}
		fen++;
	}
	while(isspace(*fen)) { fen++; }
	ep = -1; fifty = 0;
	if(*fen != '\0' && *fen != '-') ep = strsq(fen);
}
