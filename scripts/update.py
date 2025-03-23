# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from argparse import ArgumentParser
from pathlib import Path
import shutil
import filecmp

include_files = [
    "llvm-c/DataTypes.h",
    "llvm-c/Error.h",
    "llvm-c/ErrorHandling.h",
    "llvm-c/ExternC.h",
    "llvm-c/Support.h",
    "llvm-c/Types.h",
    "llvm/ADT/ADL.h",
    "llvm/ADT/APFixedPoint.h",
    "llvm/ADT/APFloat.h",
    "llvm/ADT/APInt.h",
    "llvm/ADT/APSInt.h",
    "llvm/ADT/AddressRanges.h",
    "llvm/ADT/AllocatorList.h",
    "llvm/ADT/Any.h",
    "llvm/ADT/ArrayRef.h",
    "llvm/ADT/BitVector.h",
    "llvm/ADT/Bitfields.h",
    "llvm/ADT/BitmaskEnum.h",
    "llvm/ADT/Bitset.h",
    "llvm/ADT/BreadthFirstIterator.h",
    "llvm/ADT/CachedHashString.h",
    "llvm/ADT/CoalescingBitVector.h",
    "llvm/ADT/CombinationGenerator.h",
    "llvm/ADT/ConcurrentHashtable.h",
    "llvm/ADT/DAGDeltaAlgorithm.h",
    "llvm/ADT/DeltaAlgorithm.h",
    "llvm/ADT/DeltaTree.h",
    "llvm/ADT/DenseMap.h",
    "llvm/ADT/DenseMapInfo.h",
    "llvm/ADT/DenseMapInfoVariant.h",
    "llvm/ADT/DenseSet.h",
    "llvm/ADT/DepthFirstIterator.h",
    "llvm/ADT/DirectedGraph.h",
    "llvm/ADT/DynamicAPInt.h",
    "llvm/ADT/EnumeratedArray.h",
    "llvm/ADT/EpochTracker.h",
    "llvm/ADT/EquivalenceClasses.h",
    "llvm/ADT/FloatingPointMode.h",
    "llvm/ADT/FoldingSet.h",
    "llvm/ADT/FunctionExtras.h",
    "llvm/ADT/GenericConvergenceVerifier.h",
    "llvm/ADT/GenericCycleImpl.h",
    "llvm/ADT/GenericCycleInfo.h",
    "llvm/ADT/GenericSSAContext.h",
    "llvm/ADT/GenericUniformityImpl.h",
    "llvm/ADT/GenericUniformityInfo.h",
    "llvm/ADT/GraphTraits.h",
    "llvm/ADT/Hashing.h",
    "llvm/ADT/ImmutableList.h",
    "llvm/ADT/ImmutableMap.h",
    "llvm/ADT/ImmutableSet.h",
    "llvm/ADT/IndexedMap.h",
    "llvm/ADT/IntEqClasses.h",
    "llvm/ADT/IntervalMap.h",
    "llvm/ADT/IntervalTree.h",
    "llvm/ADT/IntrusiveRefCntPtr.h",
    "llvm/ADT/LazyAtomicPointer.h",
    "llvm/ADT/MapVector.h",
    "llvm/ADT/PackedVector.h",
    "llvm/ADT/PagedVector.h",
    "llvm/ADT/PointerEmbeddedInt.h",
    "llvm/ADT/PointerIntPair.h",
    "llvm/ADT/PointerSumType.h",
    "llvm/ADT/PointerUnion.h",
    "llvm/ADT/PostOrderIterator.h",
    "llvm/ADT/PriorityQueue.h",
    "llvm/ADT/PriorityWorklist.h",
    "llvm/ADT/RewriteBuffer.h",
    "llvm/ADT/RewriteRope.h",
    "llvm/ADT/SCCIterator.h",
    "llvm/ADT/STLExtras.h",
    "llvm/ADT/STLForwardCompat.h",
    "llvm/ADT/STLFunctionalExtras.h",
    "llvm/ADT/ScopeExit.h",
    "llvm/ADT/ScopedHashTable.h",
    "llvm/ADT/Sequence.h",
    "llvm/ADT/SetOperations.h",
    "llvm/ADT/SetVector.h",
    "llvm/ADT/SlowDynamicAPInt.h",
    "llvm/ADT/SmallBitVector.h",
    "llvm/ADT/SmallPtrSet.h",
    "llvm/ADT/SmallSet.h",
    "llvm/ADT/SmallString.h",
    "llvm/ADT/SmallVector.h",
    "llvm/ADT/SmallVectorExtras.h",
    "llvm/ADT/SparseBitVector.h",
    "llvm/ADT/SparseMultiSet.h",
    "llvm/ADT/SparseSet.h",
    "llvm/ADT/StableHashing.h",
    "llvm/ADT/Statistic.h",
    "llvm/ADT/StringExtras.h",
    "llvm/ADT/StringMap.h",
    "llvm/ADT/StringMapEntry.h",
    "llvm/ADT/StringRef.h",
    "llvm/ADT/StringSet.h",
    "llvm/ADT/StringSwitch.h",
    "llvm/ADT/StringTable.h",
    "llvm/ADT/TinyPtrVector.h",
    "llvm/ADT/TrieHashIndexGenerator.h",
    "llvm/ADT/TrieRawHashMap.h",
    "llvm/ADT/Twine.h",
    "llvm/ADT/TypeSwitch.h",
    "llvm/ADT/Uniformity.h",
    "llvm/ADT/UniqueVector.h",
    "llvm/ADT/bit.h",
    "llvm/ADT/edit_distance.h",
    "llvm/ADT/fallible_iterator.h",
    "llvm/ADT/identity.h",
    "llvm/ADT/ilist.h",
    "llvm/ADT/ilist_base.h",
    "llvm/ADT/ilist_iterator.h",
    "llvm/ADT/ilist_node.h",
    "llvm/ADT/ilist_node_base.h",
    "llvm/ADT/ilist_node_options.h",
    "llvm/ADT/iterator.h",
    "llvm/ADT/iterator_range.h",
    "llvm/ADT/simple_ilist.h",
    "llvm/Demangle/Demangle.h",
    "llvm/Support/AArch64AttributeParser.h",
    "llvm/Support/AArch64BuildAttributes.h",
    "llvm/Support/AMDGPUAddrSpace.h",
    "llvm/Support/AMDGPUMetadata.h",
    "llvm/Support/AMDHSAKernelDescriptor.h",
    "llvm/Support/ARMAttributeParser.h",
    "llvm/Support/ARMBuildAttributes.h",
    "llvm/Support/ARMEHABI.h",
    "llvm/Support/ARMWinEH.h",
    "llvm/Support/AdvisoryLock.h",
    "llvm/Support/AlignOf.h",
    "llvm/Support/Alignment.h",
    "llvm/Support/Allocator.h",
    "llvm/Support/AllocatorBase.h",
    "llvm/Support/ArrayRecycler.h",
    "llvm/Support/Atomic.h",
    "llvm/Support/AtomicOrdering.h",
    "llvm/Support/AutoConvert.h",
    "llvm/Support/Automaton.h",
    "llvm/Support/BCD.h",
    "llvm/Support/BLAKE3.h",
    "llvm/Support/BalancedPartitioning.h",
    "llvm/Support/Base64.h",
    "llvm/Support/BinaryByteStream.h",
    "llvm/Support/BinaryItemStream.h",
    "llvm/Support/BinaryStream.h",
    "llvm/Support/BinaryStreamArray.h",
    "llvm/Support/BinaryStreamError.h",
    "llvm/Support/BinaryStreamReader.h",
    "llvm/Support/BinaryStreamRef.h",
    "llvm/Support/BinaryStreamWriter.h",
    "llvm/Support/BlockFrequency.h",
    "llvm/Support/BranchProbability.h",
    "llvm/Support/BuryPointer.h",
    "llvm/Support/CBindingWrapping.h",
    "llvm/Support/CFGDiff.h",
    "llvm/Support/CFGUpdate.h",
    "llvm/Support/COM.h",
    "llvm/Support/CRC.h",
    "llvm/Support/CSKYAttributeParser.h",
    "llvm/Support/CSKYAttributes.h",
    "llvm/Support/CachePruning.h",
    "llvm/Support/Caching.h",
    "llvm/Support/Capacity.h",
    "llvm/Support/Casting.h",
    "llvm/Support/CheckedArithmetic.h",
    "llvm/Support/Chrono.h",
    "llvm/Support/CodeGen.h",
    "llvm/Support/CodeGenCoverage.h",
    "llvm/Support/CommandLine.h",
    "llvm/Support/Compiler.h",
    "llvm/Support/Compression.h",
    "llvm/Support/ConvertEBCDIC.h",
    "llvm/Support/ConvertUTF.h",
    "llvm/Support/CrashRecoveryContext.h",
    "llvm/Support/DJB.h",
    "llvm/Support/DOTGraphTraits.h",
    "llvm/Support/DXILABI.h",
    "llvm/Support/DataExtractor.h",
    "llvm/Support/DataTypes.h",
    "llvm/Support/Debug.h",
    "llvm/Support/DebugCounter.h",
    "llvm/Support/Discriminator.h",
    "llvm/Support/DivisionByConstantInfo.h",
    "llvm/Support/Duration.h",
    "llvm/Support/DynamicLibrary.h",
    "llvm/Support/ELFAttrParserCompact.h",
    "llvm/Support/ELFAttrParserExtended.h",
    "llvm/Support/ELFAttributeParser.h",
    "llvm/Support/ELFAttributes.h",
    "llvm/Support/Endian.h",
    "llvm/Support/EndianStream.h",
    "llvm/Support/Errc.h",
    "llvm/Support/Errno.h",
    "llvm/Support/Error.h",
    "llvm/Support/ErrorHandling.h",
    "llvm/Support/ErrorOr.h",
    "llvm/Support/ExitCodes.h",
    "llvm/Support/ExponentialBackoff.h",
    "llvm/Support/ExtensibleRTTI.h",
    "llvm/Support/FileCollector.h",
    "llvm/Support/FileOutputBuffer.h",
    "llvm/Support/FileSystem.h",
    "llvm/Support/FileSystem/UniqueID.h",
    "llvm/Support/FileUtilities.h",
    "llvm/Support/Format.h",
    "llvm/Support/FormatAdapters.h",
    "llvm/Support/FormatCommon.h",
    "llvm/Support/FormatProviders.h",
    "llvm/Support/FormatVariadic.h",
    "llvm/Support/FormatVariadicDetails.h",
    "llvm/Support/FormattedStream.h",
    "llvm/Support/GenericDomTree.h",
    "llvm/Support/GenericDomTreeConstruction.h",
    "llvm/Support/GenericIteratedDominanceFrontier.h",
    "llvm/Support/GenericLoopInfo.h",
    "llvm/Support/GenericLoopInfoImpl.h",
    "llvm/Support/GlobPattern.h",
    "llvm/Support/GraphWriter.h",
    "llvm/Support/HashBuilder.h",
    "llvm/Support/HexagonAttributeParser.h",
    "llvm/Support/HexagonAttributes.h",
    "llvm/Support/InitLLVM.h",
    "llvm/Support/InstructionCost.h",
    "llvm/Support/JSON.h",
    "llvm/Support/KnownBits.h",
    "llvm/Support/LEB128.h",
    "llvm/Support/LLVMDriver.h",
    "llvm/Support/LineIterator.h",
    "llvm/Support/Locale.h",
    "llvm/Support/LockFileManager.h",
    "llvm/Support/LogicalResult.h",
    "llvm/Support/MD5.h",
    "llvm/Support/MSP430AttributeParser.h",
    "llvm/Support/MSP430Attributes.h",
    "llvm/Support/MSVCErrorWorkarounds.h",
    "llvm/Support/ManagedStatic.h",
    "llvm/Support/MathExtras.h",
    "llvm/Support/MemAlloc.h",
    "llvm/Support/Memory.h",
    "llvm/Support/MemoryBuffer.h",
    "llvm/Support/MemoryBufferRef.h",
    "llvm/Support/MipsABIFlags.h",
    "llvm/Support/ModRef.h",
    "llvm/Support/Mutex.h",
    "llvm/Support/NVPTXAddrSpace.h",
    "llvm/Support/NativeFormatting.h",
    "llvm/Support/OnDiskHashTable.h",
    "llvm/Support/OptimizedStructLayout.h",
    "llvm/Support/OptionStrCmp.h",
    "llvm/Support/PGOOptions.h",
    "llvm/Support/Parallel.h",
    "llvm/Support/Path.h",
    "llvm/Support/PerThreadBumpPtrAllocator.h",
    "llvm/Support/PluginLoader.h",
    "llvm/Support/PointerLikeTypeTraits.h",
    "llvm/Support/PrettyStackTrace.h",
    "llvm/Support/Printable.h",
    "llvm/Support/Process.h",
    "llvm/Support/Program.h",
    "llvm/Support/RISCVAttributeParser.h",
    "llvm/Support/RISCVAttributes.h",
    "llvm/Support/RISCVISAUtils.h",
    "llvm/Support/RWMutex.h",
    "llvm/Support/RandomNumberGenerator.h",
    "llvm/Support/Recycler.h",
    "llvm/Support/RecyclingAllocator.h",
    "llvm/Support/Regex.h",
    "llvm/Support/Registry.h",
    "llvm/Support/ReverseIteration.h",
    "llvm/Support/SHA1.h",
    "llvm/Support/SHA256.h",
    "llvm/Support/SMLoc.h",
    "llvm/Support/SMTAPI.h",
    "llvm/Support/SaveAndRestore.h",
    "llvm/Support/ScaledNumber.h",
    "llvm/Support/ScopedPrinter.h",
    "llvm/Support/Signals.h",
    "llvm/Support/Signposts.h",
    "llvm/Support/SipHash.h",
    "llvm/Support/SmallVectorMemoryBuffer.h",
    "llvm/Support/SourceMgr.h",
    "llvm/Support/SpecialCaseList.h",
    "llvm/Support/StringSaver.h",
    "llvm/Support/SuffixTree.h",
    "llvm/Support/SuffixTreeNode.h",
    "llvm/Support/SwapByteOrder.h",
    "llvm/Support/SystemUtils.h",
    "llvm/Support/SystemZ/zOSSupport.h",
    "llvm/Support/TarWriter.h",
    "llvm/Support/TargetOpcodes.def",
    "llvm/Support/TargetSelect.h",
    "llvm/Support/ThreadPool.h",
    "llvm/Support/ThreadSafeAllocator.h",
    "llvm/Support/Threading.h",
    "llvm/Support/TimeProfiler.h",
    "llvm/Support/Timer.h",
    "llvm/Support/ToolOutputFile.h",
    "llvm/Support/TrailingObjects.h",
    "llvm/Support/TypeName.h",
    "llvm/Support/TypeSize.h",
    "llvm/Support/Unicode.h",
    "llvm/Support/UnicodeCharRanges.h",
    "llvm/Support/Valgrind.h",
    "llvm/Support/VersionTuple.h",
    "llvm/Support/VirtualFileSystem.h",
    "llvm/Support/Watchdog.h",
    "llvm/Support/Win64EH.h",
    "llvm/Support/WindowsError.h",
    "llvm/Support/WithColor.h",
    "llvm/Support/X86DisassemblerDecoderCommon.h",
    "llvm/Support/X86FoldTablesUtils.h",
    "llvm/Support/YAMLParser.h",
    "llvm/Support/YAMLTraits.h",
    "llvm/Support/circular_raw_ostream.h",
    "llvm/Support/float128.h",
    "llvm/Support/raw_os_ostream.h",
    "llvm/Support/raw_ostream.h",
    "llvm/Support/raw_sha1_ostream.h",
    "llvm/Support/raw_socket_stream.h",
    "llvm/Support/thread.h",
    "llvm/Support/type_traits.h",
    "llvm/Support/xxhash.h",
]

src_files = [
    # "Support/AArch64AttributeParser.cpp",
    # "Support/AArch64BuildAttributes.cpp",
    "Support/ABIBreak.cpp",
    "Support/AMDGPUMetadata.cpp",
    "Support/APFixedPoint.cpp",
    "Support/APFloat.cpp",
    "Support/APInt.cpp",
    "Support/APSInt.cpp",
    # "Support/ARMAttributeParser.cpp",
    # "Support/ARMBuildAttributes.cpp",
    "Support/ARMWinEH.cpp",
    "Support/Allocator.cpp",
    "Support/Atomic.cpp",
    "Support/AutoConvert.cpp",
    "Support/BalancedPartitioning.cpp",
    "Support/Base64.cpp",
    "Support/BinaryStreamError.cpp",
    "Support/BinaryStreamReader.cpp",
    "Support/BinaryStreamRef.cpp",
    "Support/BinaryStreamWriter.cpp",
    "Support/BlockFrequency.cpp",
    "Support/BranchProbability.cpp",
    "Support/BuryPointer.cpp",
    "Support/COM.cpp",
    "Support/CRC.cpp",
    # "Support/CSKYAttributeParser.cpp",
    # "Support/CSKYAttributes.cpp",
    "Support/CachePruning.cpp",
    "Support/Caching.cpp",
    "Support/Chrono.cpp",
    "Support/CodeGenCoverage.cpp",
    "Support/CommandLine.cpp",
    "Support/Compression.cpp",
    "Support/ConvertEBCDIC.cpp",
    "Support/ConvertUTF.cpp",
    "Support/ConvertUTFWrapper.cpp",
    "Support/CrashRecoveryContext.cpp",
    "Support/DAGDeltaAlgorithm.cpp",
    "Support/DJB.cpp",
    "Support/DataExtractor.cpp",
    "Support/Debug.cpp",
    "Support/DebugCounter.cpp",
    "Support/DebugOptions.h",
    "Support/DeltaAlgorithm.cpp",
    "Support/DeltaTree.cpp",
    "Support/DivisionByConstantInfo.cpp",
    # "Support/DynamicAPInt.cpp",
    "Support/DynamicLibrary.cpp",
    # "Support/ELFAttrParserCompact.cpp",
    # "Support/ELFAttrParserExtended.cpp",
    # "Support/ELFAttributes.cpp",
    "Support/Errno.cpp",
    "Support/Error.cpp",
    "Support/ErrorHandling.cpp",
    "Support/ExponentialBackoff.cpp",
    "Support/ExtensibleRTTI.cpp",
    "Support/FileCollector.cpp",
    "Support/FileOutputBuffer.cpp",
    "Support/FileUtilities.cpp",
    "Support/FloatingPointMode.cpp",
    "Support/FoldingSet.cpp",
    "Support/FormatVariadic.cpp",
    "Support/FormattedStream.cpp",
    "Support/GlobPattern.cpp",
    "Support/GraphWriter.cpp",
    # "Support/HexagonAttributeParser.cpp",
    # "Support/HexagonAttributes.cpp",
    "Support/InitLLVM.cpp",
    "Support/InstructionCost.cpp",
    "Support/IntEqClasses.cpp",
    "Support/IntervalMap.cpp",
    "Support/JSON.cpp",
    "Support/KnownBits.cpp",
    "Support/LEB128.cpp",
    "Support/LineIterator.cpp",
    "Support/Locale.cpp",
    "Support/LockFileManager.cpp",
    "Support/MD5.cpp",
    # "Support/MSP430AttributeParser.cpp",
    # "Support/MSP430Attributes.cpp",
    "Support/ManagedStatic.cpp",
    "Support/MathExtras.cpp",
    "Support/MemAlloc.cpp",
    "Support/Memory.cpp",
    "Support/MemoryBuffer.cpp",
    "Support/MemoryBufferRef.cpp",
    "Support/ModRef.cpp",
    "Support/NativeFormatting.cpp",
    "Support/OptimizedStructLayout.cpp",
    "Support/OptionStrCmp.cpp",
    "Support/Optional.cpp",
    "Support/PGOOptions.cpp",
    "Support/Parallel.cpp",
    "Support/Path.cpp",
    "Support/PluginLoader.cpp",
    "Support/PrettyStackTrace.cpp",
    "Support/Process.cpp",
    "Support/Program.cpp",
    # "Support/RISCVAttributeParser.cpp",
    # "Support/RISCVAttributes.cpp",
    "Support/RISCVISAUtils.cpp",
    "Support/RWMutex.cpp",
    "Support/RandomNumberGenerator.cpp",
    "Support/Regex.cpp",
    # "Support/RewriteBuffer.cpp",
    # "Support/RewriteRope.cpp",
    "Support/SHA1.cpp",
    "Support/SHA256.cpp",
    "Support/ScaledNumber.cpp",
    "Support/ScopedPrinter.cpp",
    "Support/Signals.cpp",
    "Support/Signposts.cpp",
    "Support/SipHash.cpp",
    # "Support/SlowDynamicAPInt.cpp",
    "Support/SmallPtrSet.cpp",
    "Support/SmallVector.cpp",
    "Support/SourceMgr.cpp",
    "Support/SpecialCaseList.cpp",
    "Support/Statistic.cpp",
    "Support/StringExtras.cpp",
    "Support/StringMap.cpp",
    "Support/StringRef.cpp",
    "Support/StringSaver.cpp",
    "Support/SuffixTree.cpp",
    "Support/SuffixTreeNode.cpp",
    "Support/SystemUtils.cpp",
    "Support/TarWriter.cpp",
    "Support/ThreadPool.cpp",
    "Support/Threading.cpp",
    "Support/TimeProfiler.cpp",
    "Support/Timer.cpp",
    "Support/ToolOutputFile.cpp",
    "Support/TrieRawHashMap.cpp",
    "Support/Twine.cpp",
    "Support/TypeSize.cpp",
    "Support/Unicode.cpp",
    "Support/UnicodeCaseFold.cpp",
    "Support/UnicodeNameToCodepoint.cpp",
    "Support/UnicodeNameToCodepointGenerated.cpp",
    "Support/Unix/COM.inc",
    "Support/Unix/DynamicLibrary.inc",
    "Support/Unix/Memory.inc",
    "Support/Unix/Path.inc",
    "Support/Unix/Process.inc",
    "Support/Unix/Program.inc",
    "Support/Unix/Signals.inc",
    "Support/Unix/Threading.inc",
    "Support/Unix/Unix.h",
    "Support/Unix/Watchdog.inc",
    "Support/Valgrind.cpp",
    "Support/VersionTuple.cpp",
    "Support/VirtualFileSystem.cpp",
    "Support/Watchdog.cpp",
    "Support/Windows/Path.inc",
    "Support/Windows/Process.inc",
    "Support/Windows/Program.inc",
    "Support/Windows/Signals.inc",
    "Support/Windows/Threading.inc",
    "Support/WithColor.cpp",
    "Support/YAMLParser.cpp",
    "Support/YAMLTraits.cpp",
    "Support/Z3Solver.cpp",
    "Support/circular_raw_ostream.cpp",
    "Support/raw_os_ostream.cpp",
    "Support/raw_ostream.cpp",
    "Support/raw_socket_stream.cpp",
    "Support/regcomp.c",
    "Support/regengine.inc",
    "Support/regerror.c",
    "Support/regex2.h",
    "Support/regex_impl.h",
    "Support/regexec.c",
    "Support/regfree.c",
    "Support/regstrlcpy.c",
    "Support/regutils.h",
    "Support/xxhash.cpp",
]

test_files = [
    "ADT/CountCopyAndMove.cpp",
    "ADT/CountCopyAndMove.h",
    "ADT/DenseMapTest.cpp",
    "ADT/STLExtrasTest.cpp",
    "ADT/SmallVectorTest.cpp",
]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("llvm_root")
    parser.add_argument("dst_dir")

    args = parser.parse_args()
    llvm_include_dir = Path(args.llvm_root) / "llvm" / "include"
    llvm_src_dir = Path(args.llvm_root) / "llvm" / "lib"
    llvm_test_dir = Path(args.llvm_root) / "llvm" / "unittests"

    dst_dir = Path(args.dst_dir)
    include_dir = dst_dir / "include"
    src_dir = dst_dir / "lib"
    test_dir = dst_dir / "tests"

    dirs = [
        (include_dir, llvm_include_dir, include_files),
        (src_dir, llvm_src_dir, src_files),
        (test_dir, llvm_test_dir, test_files),
    ]

    for dst, src, files in dirs:
        dst.mkdir(parents=True, exist_ok=True)
        for file in files:
            file = Path(file)
            dst_path = dst / file.parent
            src_file = src / file
            dst_file = dst / file
            if dst_file.exists() and filecmp.cmp(src_file, dst_file):
                print(f'"{dst_file}" is up to date')
                continue

            print(f'Copying "{file}" to "{dst}"')
            dst_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(src=src_file, dst=dst_path)

    # Amalgamate lib sources
    print("Amalgamating lib sources")
    with open(src_dir / "Support.cpp", "w") as f:
        for file in src_files:
            if not file.endswith(".cpp"):
                continue

            f.write(f'#include "{file}"\n')
            f.write("#undef DEBUG_TYPE\n")

    with open(src_dir / "Support.c", "w") as f:
        for file in src_files:
            if not file.endswith(".c"):
                continue

            f.write(f'#include "{file}"\n')

    print("Done")
